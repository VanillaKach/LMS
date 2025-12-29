from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import Group
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from .models import CustomUser, Payment
from .serializers import UserSerializer, PaymentSerializer

class UserProfileView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_permissions(self):
        if self.request.user == self.get_object():
            permission_classes = [IsAuthenticated]
        else:
            # Показываем только ограниченные поля
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']
    ordering = ['-payment_date']
