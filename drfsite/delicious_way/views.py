from django.forms.models import model_to_dict
from rest_framework import generics
from .models import DeliciousWay
from django.shortcuts import render
from .serializer import DeliciousWaySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class DeliciousWayAPIView(APIView):
    def get(self, request):
        lst = DeliciousWay.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = DeliciousWay.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': model_to_dict(post_new)})

# class DeliciousWayAPIView(generics.ListAPIView):
#     queryset = DeliciousWay.objects.all()
#     serializer_class = DeliciousWaySerializer
