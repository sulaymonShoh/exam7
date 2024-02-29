from django import forms

from apps.store.models import Product


class ProductForm(forms.ModelForm):
    photo = forms.FileField()

    class Meta:
        model = Product
        fields = ('name', 'description', 'author', 'category', 'owner_full_name', 'owner_username', 'end_date', 'price',
                  'price_in_dollar', 'photo')
