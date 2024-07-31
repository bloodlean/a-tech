from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search_view, name='search_view'),
    path('onlinestore/', views.onlinestore, name='onlinestore'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)