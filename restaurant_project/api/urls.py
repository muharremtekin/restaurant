from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'menu-items', views.MenuItemViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'reservations', views.ReservationViewSet, basename='reservation')
router.register(r'orders', views.OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuListView.as_view(), name='menu_list'),
    path('reservation/', views.ReservationCreateView.as_view(), name='reservation_create'),
]