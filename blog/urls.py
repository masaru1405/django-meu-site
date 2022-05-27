from django.urls import path
from . import views

urlpatterns = [
   path('', views.BlogListView.as_view(), name='blog.home'),
   path('<slug:slug>/', views.BlogDetailView.as_view(), name='post.detail'), #vídeo 2h51m
]