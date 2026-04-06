from django.urls import path
from .views import StudentCreateView, success_view

urlpatterns = [
    path('', StudentCreateView.as_view(), name='form'),
    path('success/', success_view, name='success'),
]