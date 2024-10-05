from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Author
from .forms import PostForm
from django.urls import reverse, reverse_lazy
def index(request):
    context = {'massage':'hello'}
    return render(request, 'index.html',context)

def home_page(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    context = {'posts':posts, 'author':authors}
    return render(request, 'home_page.html',context)

def add_post(request):

    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            saved = form.save(commit=False)
            saved.create_data = datetime.now()
            saved.update_data = datetime.now()

            saved.save()
            return HttpResponseRedirect(reverse_lazy('add_post'))

    return render(request, 'add_post.html', {'form':form})


def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request,'post_detail.html',context)


def author_page(request, pk):
    author = Author.objects.get(pk=pk)
    authors_posts = Post.objects.filter(author=author)
    context = {'author':author,'authors_posts':authors_posts}
    return render(request, 'author_page.html',context)

def add_like(request,pk):
    post = Post.objects.get(pk=pk)
    post.numbers_of_likes +=1
    post.save()
    return render(request, 'post_detail.html', {'post': post})

