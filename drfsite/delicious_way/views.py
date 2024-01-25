from django.forms.models import model_to_dict
from rest_framework import generics, viewsets, mixins
from .models import DeliciousWay
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import DeliciousWay, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import DeliciousWaySerializer


class DeliciousWayAPIList(generics.ListCreateAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer
    #permission_classes = (IsAuthenticatedOrReadOnly,)


class DeliciousWayAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer
    permission_classes = (IsOwnerOrReadOnly,)


class DeliciousWayAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer
    permission_classes = (IsAdminOrReadOnly,)



