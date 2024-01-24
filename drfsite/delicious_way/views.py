from django.forms.models import model_to_dict
from rest_framework import generics, viewsets, mixins
from .models import DeliciousWay
from django.shortcuts import render
from rest_framework.decorators import action
from .serializer import DeliciousWaySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import DeliciousWay, Category


class DeliciousWayViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    #queryset = DeliciousWay.objects.all()
    serializer_class = DeliciousWaySerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return DeliciousWay.objects.all()[:3]

        return DeliciousWay.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class DeliciousWayAPIList(generics.ListCreateAPIView):
#     queryset = DeliciousWay.objects.all()
#     serializer_class = DeliciousWaySerializer
#
#
# class DeliciousWayAPIUpdate(generics.UpdateAPIView):
#     queryset = DeliciousWay.objects.all()
#     serializer_class = DeliciousWaySerializer
#
#
# class DeliciousWayAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DeliciousWay.objects.all()
#     serializer_class = DeliciousWaySerializer


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
