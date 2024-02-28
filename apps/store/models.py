from django.db import models

from apps.accounts.models import User
from apps.shared.models import AbstractModel


class Category(AbstractModel):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(AbstractModel):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, models.CASCADE, "products")
    category = models.ForeignKey(Category, models.CASCADE, "products")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_in_dollar = models.DecimalField(max_digits=10, decimal_places=2)
    end_date = models.DateTimeField()
    photo = models.FileField(upload_to="products/photo/%Y/%m/%d", default="default/discover-04.jpg")

    def __str__(self):
        return "{0} by {1}".format(self.name, self.owner)
