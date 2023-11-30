from rest_framework import generics
from .models import DeliciousWay
from django.shortcuts import render
from .serializer import DeliciousWaySerializer


class DeliciousWayAPIView(generics.ListAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer
