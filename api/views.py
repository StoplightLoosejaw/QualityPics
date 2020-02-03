from django.shortcuts import render
from .models import Pic
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
import random
from .forms import LoginForm
from braces import views
from django.http import HttpResponse


# Create your views here.

def Home(request):
    queryset = Pic.objects.all()
    maxval = len(queryset)
    return render(request, 'home.html', { 'maxval': maxval})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'logout.html')
    
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

class PicListView(views.LoginRequiredMixin,
                  views.SuperuserRequiredMixin,
                  generics.ListCreateAPIView):
        queryset = Pic.objects.all()
        serializer_class = serializers.PicSerializer

class SinglePicView(generics.RetrieveAPIView):
        queryset = Pic.objects.all()
        serializer_class = serializers.PicSerializer
