from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem, Category, Reservation, Order, Table
from .serializers import MenuItemSerializer, CategorySerializer, ReservationSerializer, OrderSerializer
from datetime import datetime, timedelta

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['special_items'] = MenuItem.objects.filter(is_special=True)[:3]
        return context

class MenuListView(ListView):
    template_name = 'menu/list.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class ReservationCreateView(TemplateView):
    template_name = 'reservation/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.today().date()
        context['max_date'] = (datetime.today() + timedelta(days=30)).date()
        return context

# API Views
class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset

class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Rezervasyon validasyonu
        date = request.data.get('date')
        time = request.data.get('time')
        party_size = request.data.get('party_size')

        if not all([date, time, party_size]):
            return Response(
                {'error': 'Tarih, saat ve kişi sayısı gereklidir.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Masa müsaitlik kontrolü
        available_tables = Table.objects.filter(
            capacity__gte=party_size
        ).exclude(
            reservation__date=date,
            reservation__time=time,
            reservation__status='confirmed'
        )

        if not available_tables.exists():
            return Response(
                {'error': 'Seçilen tarih ve saatte uygun masa bulunmamaktadır.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Toplam tutarı hesapla
        items = self.request.data.get('items', [])
        total = sum(
            item.get('quantity', 0) * MenuItem.objects.get(
                id=item.get('menu_item')
            ).price
            for item in items
        )
        serializer.save(user=self.request.user, total_amount=total)