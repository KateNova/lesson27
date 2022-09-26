import json
import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avito.settings')
application = get_wsgi_application()

from ads.models import Ad, Category

with open("ads.json", "r") as f:
    ads_list = json.load(f)

for ad in ads_list:
    obj = Ad()
    obj.name = ad['name']
    obj.author = ad['author']
    obj.price = int(ad['price'])
    obj.description = ad['description']
    obj.address = ad['address']

    if ad['is_published'] == 'TRUE':
        obj.is_published = True
    else:
        obj.is_published = False

    obj.save()

with open("categories.json", "r") as f:
    cat_list = json.load(f)

for cat in cat_list:
    obj = Category()
    obj.name = cat['name']

    obj.save()
