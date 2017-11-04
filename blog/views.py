from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from rest_framework.generics import ListAPIView
from .serializers import  postSerializer
# Create your views here.


def home(request):
    return HttpResponse("Hello world")


def listview(request):
    objs = post.objects.all()
    return render(request,'index.html',{'posts':objs})

def detailview(request,pk):
    obj=post.objects.get(pk=pk)
    return render(request,'detail.html',{'post':obj})

def listviewAPI(ListAPIView):
    queryset = post.objects.all()
    serializers_class = postSerializer

