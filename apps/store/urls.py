from django.urls import path

from apps.store.views import HomeView, ExploreView, AuthorDetailView, ProductDetailView, ProductCreateView, \
    ProductUpdateView

app_name = "store"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('explore/', ExploreView.as_view(), name="explore"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('author/<str:username>', AuthorDetailView.as_view(), name="author_detail"),
    path('products/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name="product_update"),

]