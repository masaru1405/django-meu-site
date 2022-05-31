from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from .forms import PostForm

class BlogListView(ListView):
   model = Post
   template_name = 'blog/home.html'
   context_object_name = 'posts'

class BlogDetailView(DetailView):
   model = Post
   template_name = 'blog/detail.html'
   context_object_name = 'post'

#video 2h52m
class BlogCreateView(SuccessMessageMixin, CreateView):
   model = Post
   template_name = 'blog/new.html'
   #fields = '__all__'
   fields = ['title', 'content', 'author']
   success_message = "%(field)s criado com sucesso!"
   
   #video 3h37
   def get_success_message(self, cleaned_data):
      return self.success_message % dict(
         cleaned_data,
         field=self.object.title,
      )

class BlogUpdateView(SuccessMessageMixin, UpdateView):
   model = Post
   form_class = PostForm
   template_name = 'blog/edit.html'
   #fields = ['title', 'content']
   success_message = "%(field)s alterado com sucesso!" #field neste caso será o atributo 'title', ver abaixo

   def get_success_message(self, cleaned_data):
      return self.success_message % dict(
         cleaned_data,
         field=self.object.title,
      )

class BlogDeleteView(SuccessMessageMixin, DeleteView):
   model = Post
   template_name = 'blog/delete.html'
   context_object_name = 'post'
   success_url = reverse_lazy('blog.home')
   success_message = "%(field)s deletado com sucesso!"

   #video 3h37
   def get_success_message(self, cleaned_data):
      return self.success_message % dict(
         cleaned_data,
         field=self.object.title,
      )