from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
   model = Post
   template_name = 'blog/home.html'
   context_object_name = 'posts'

class BlogDetailView(DetailView):
   model = Post
   template_name = 'blog/detail.html'
   context_object_name = 'post'

#2h52m
class BlogCreateView(CreateView):
   model = Post
   template_name = 'blog/new.html'
   fields = '__all__'

class BlogUpdateView(UpdateView):
   model = Post
   template_name = 'blog/edit.html'
   fields = ('title', 'content')

class BlogDeleteView(DeleteView):
   model = Post
   template_name = 'blog/delete.html'
   context_object_name = 'post'
   success_url = reverse_lazy('blog.home')