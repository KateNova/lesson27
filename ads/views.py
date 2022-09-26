import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt

from ads.models import Category, Ad


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        cats = Category.objects.all()

        search_text = request.GET.get("name", None)
        if search_text:
            cats = cats.filter(name=search_text)

        response = []
        for cat in cats:
            response.append({
                "id": cat.id,
                "name": cat.name,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        cat = Category.objects.create(
            name=data["name"],
        )

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        }, status=201)


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            cat = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()

        search_text = request.GET.get("name", None)
        if search_text:
            ads = ads.filter(name=search_text)

        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        ad = Ad.objects.create(
            name=data["name"],
            author=data["author"],
            price=data["price"],
            description=data["description"],
            address=data["address"],
            is_published=data["is_published"]
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        }, status=201)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })
