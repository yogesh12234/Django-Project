from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render, redirect
from .models import Product, Category
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from app2.models import Category
Category.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']
    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAdminUser()]
        return [IsAuthenticated()]

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_list(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')

        print(name, price, category_id)  # 👈 DEBUG

        if name and price and category_id:
            category = Category.objects.get(id=category_id)

            Product.objects.create(
                name=name,
                price=price,
                category=category
            )

            return redirect('product_list')
        else:
            print("FORM DATA MISSING ❌")

    products = Product.objects.all()

    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories
    })

def delete_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect('product_list')