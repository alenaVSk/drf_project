from django.forms.models import model_to_dict
from rest_framework import generics
from .models import DeliciousWay
from django.shortcuts import render
from .serializer import DeliciousWaySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class DeliciousWayAPIList(generics.ListCreateAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer


class DeliciousWayAPIUpdate(generics.UpdateAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer


class DeliciousWayAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer


# class DeliciousWayAPIView(APIView):
#     def get(self, request):
#         w = DeliciousWay.objects.all().values()
#         return Response({'posts': DeliciousWaySerializer(w, many=True).data})
#
#
#     def post(self, request):
#         serializer = DeliciousWaySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = DeliciousWay.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = DeliciousWaySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = DeliciousWay.objects.get(pk=pk)
#             instance.delete()
#
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"post": "delete post " + str(pk)})


# class DeliciousWayAPIView(generics.ListAPIView):
#     queryset = DeliciousWay.objects.all()
#     serializer_class = DeliciousWaySerializer
