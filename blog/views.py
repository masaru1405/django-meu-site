from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from .forms import PostForm

#6h46m
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(ListView):
   model = Post
   template_name = 'blog/home.html'
   context_object_name = 'posts'

class BlogDetailView(DetailView):
   model = Post
   template_name = 'blog/detail.html'
   context_object_name = 'post'

#video 2h52m
class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   model = Post
   form_class = PostForm
   template_name = 'blog/new.html'
   #fields = '__all__'
   #fields = ['title', 'content', 'author']
   success_message = "%(field)s criado com sucesso!"

   #video 6h14
   #author será o user logado
   def form_valid(self, form):
      obj = form.save(commit=False)
      obj.author = self.request.user
      obj.save()
      return super().form_valid(form)
   
   #video 3h37
   def get_success_message(self, cleaned_data):
      return self.success_message % dict(
         cleaned_data,
         field=self.object.title,
      )

#OBS: neste caso não precisamos especificar a url da tela de login, pois estamos usando o login.html do Django ?
#ou seja, o 'User' padrão 
class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = Post
   form_class = PostForm
   template_name = 'blog/edit.html'
   #fields = ['title', 'content']
   success_message = "%(field)s alterado com sucesso!" #field neste caso será o atributo 'title', ver abaixo

   #video 6h14
   #author será o user logado
   def form_valid(self, form):
      obj = form.save(commit=False)
      obj.author = self.request.user
      obj.save()
      return super().form_valid(form)

   def get_success_message(self, cleaned_data):
      return self.success_message % dict(
         cleaned_data,
         field=self.object.title,
      )

class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
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