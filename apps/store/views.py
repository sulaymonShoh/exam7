from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView

from apps.accounts.models import User
from apps.store.forms import ProductForm
from apps.store.models import Product, Category


class HomeView(View):
    def get(self, request):
        products = Product.objects.order_by("-created_at")[:8]
        return render(request, 'store/index.html', {"products": products})


class ExploreView(View):
    def get(self, request):
        categories = Category.objects.all()
        top_products = [Product.objects.filter(category=i).order_by('-created_at').first() for i in categories]
        products = Product.objects.order_by("-created_at")[:8]
        return render(request, 'store/explore.html', {"products": products, "top_products": top_products})


class AuthorDetailView(LoginRequiredMixin, View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        products = Product.objects.filter(author=user)
        return render(request, 'store/author.html', context={"author": user, "products": products})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'store/details.html', {"product": product})


class ProductCreateView(CreateView):
    template_name = 'store/create.html'
    form_class = ProductForm
    model = Product
    # fields = ('name', 'description', 'author', 'category', 'owner_full_name', 'owner_username', 'end_date', 'price',
              # 'price_in_dollar', 'photo')
    success_url = reverse_lazy("store:home")


class ProductUpdateView(UpdateView):
    template_name = 'store/create.html'
    form_class = ProductForm
    model = Product
    # fields = ('name', 'description', 'author', 'category', 'owner_full_name', 'owner_username', 'end_date', 'price',
              # 'price_in_dollar', 'photo')
    success_url = reverse_lazy("store:home")
