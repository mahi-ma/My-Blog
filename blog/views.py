from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Post
from django.views import generic
from django.views.generic import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from rest_framework.generics import ListAPIView
from .serializers import  postSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    return HttpResponse("Hello world")


def listview(request):
    objs = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':objs})


def detailview(request,pk):
    obj=Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'post':obj})

def searchview(request):
    entry = get_object_or_404(Post, title=request.GET.get("q"))
    return render(request, 'blog/search.html', {'entry': entry})

def listviewAPI(ListAPIView):
    queryset = Post.objects.all()
    serializers_class = postSerializer


class PostCreate(CreateView):
    model = Post
    fields = ['title','description']

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','description']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:listview')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog:listview')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})