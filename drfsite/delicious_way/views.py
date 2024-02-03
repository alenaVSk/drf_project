from django.forms.models import model_to_dict
from rest_framework import generics, viewsets, mixins
from .models import DeliciousWay
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import DeliciousWay, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import DeliciousWaySerializer


class DeliciousWayAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class DeliciousWayAPIList(generics.ListCreateAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = DeliciousWayAPIListPagination


class DeliciousWayAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DeliciousWayAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer
    permission_classes = (IsAdminOrReadOnly,)



