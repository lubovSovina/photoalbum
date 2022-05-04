from django.http import Http404
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PhotoSerializer, PhotoSmallSerializer
from .models import Photo


class GetListAllPhoto(generics.ListAPIView):
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Photo.objects.all()


class CreatePhoto(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        serializer = PhotoSmallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemPhotoViews(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PhotoSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        serializer = PhotoSmallSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = PhotoSmallSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPhotosByUsers(ListModelMixin, GenericAPIView):
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Photo.objects.filter(user_id=pk)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
