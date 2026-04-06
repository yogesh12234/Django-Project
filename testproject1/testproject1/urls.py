from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app3.views import ProductViewSet
from app4.views import OrderViewSet
from app1.views import home
from app1.views import login_view, register_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', include('app3.urls')),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    # API URLs (change here)
    path('api/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]