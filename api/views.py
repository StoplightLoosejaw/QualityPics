from django.shortcuts import render
from .models import Pic
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
import random

# Create your views here.

from django.shortcuts import render

def Home(request):
    queryset = Pic.objects.all()
    maxval = len(queryset)
    return render(request, 'home.html', { 'maxval': maxval})

class RandomPicView(generics.RetrieveAPIView):
    queryset = Pic.objects.all()
    serializer_class = serializers.PicSerializer

    def retrieve(self, request):
            queryset = Pic.objects.all()
            pk = random.randint(1,len(queryset))
            pic = Pic.objects.get(pk=pk)
            serializer = serializers.PicSerializer(pic)
            data = serializer.data
            return Response(data)

class PicListView(generics.ListCreateAPIView):
        queryset = Pic.objects.all()
        serializer_class = serializers.PicSerializer

class SinglePicView(generics.RetrieveAPIView):
        queryset = Pic.objects.all()
        serializer_class = serializers.PicSerializer

class CategoryPicView(generics.ListCreateAPIView):
        queryset = Pic.objects.all()
        serializer_class = serializers.PicSerializer

        def list(self, request, **kwargs):
                queryset = Pic.objects.filter(**kwargs)
                serializer = serializers.PicSerializer(queryset, many=True)
                data = serializer.data
                return Response(serializer.data)
