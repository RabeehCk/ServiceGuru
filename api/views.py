from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework import authentication,permissions

from api.serializers import CustomerSerializer

from api.models import Customer


class CustomerViewSetView(ModelViewSet):

    serializer_class = CustomerSerializer

    queryset = Customer.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        
        serializer.save(technician=self.request.user)

        




