from django.forms.models import model_to_dict
from rest_framework import generics
from .models import DeliciousWay
from django.shortcuts import render
from .serializer import DeliciousWaySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class DeliciousWayAPIView(APIView):
    def get(self, request):
        w = DeliciousWay.objects.all().values()
        return Response({'posts': DeliciousWaySerializer(w, many=True).data})


    def post(self, request):
        serializer = DeliciousWaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = DeliciousWay.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': DeliciousWaySerializer(post_new).data})

# class DeliciousWayAPIView(generics.ListAPIView):
#     queryset = DeliciousWay.objects.all()
#     serializer_class = DeliciousWaySerializer
