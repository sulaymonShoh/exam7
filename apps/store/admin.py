from django.contrib import admin
from apps.store.models import Product, Category

admin.site.register([Product, Category])
