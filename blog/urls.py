from django.urls import path
from . import views

urlpatterns = [
   path('', views.BlogListView.as_view(), name='blog.home'),
   path('new/', views.BlogCreateView.as_view(), name='post.new'), #3h07 ver o problema relacionado ao uso de slug
   path('<slug:slug>/', views.BlogDetailView.as_view(), name='post.detail'), #vídeo 2h51m
   path('<slug:slug>/edit/', views.BlogUpdateView.as_view(), name='post.edit'),
]