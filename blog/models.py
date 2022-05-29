from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#video 3h50
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS = [('draft', 'Draft'), ('published', 'Published')]

class PublishedManager(models.Manager):
   def get_queryset(self):
      return super(PublishedManager, self).get_queryset()\
                                          .filter(status='published')

class Post(models.Model):
   title = models.CharField(max_length=200)
   slug = models.SlugField(max_length=200)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   content = models.TextField()
   published_at = models.DateTimeField(default=timezone.now)
   created_at = models.DateTimeField(auto_now_add=True)#só irá add a data na 1ª vez | campo oculto
   modified_at = models.DateTimeField(auto_now=True)#campo oculto
   status = models.CharField(max_length=20, choices=STATUS, default='draft')

   ###Opcional###
   #Sem essa linha, só irá mostar os posts com status='published', por causa da linha 28 (ver vídeo: 2h:07)
   objects = models.Manager()

   #Ex: Post.published.all() irá retornar todos os Posts que tenham o status='published'(vídeo: 2h:02)
   #Poderíamos fazer: Post.objects.all().filter(status='published')
   published = PublishedManager()

   #Vídeo 2h51m
   def get_absolute_url(self):
      return reverse('post.detail', args=[self.slug])

   class Meta:
      ordering = ('-published_at',)#irá mostrar os mais recentes antes

   def __str__(self):
      return "{} - {}".format(self.title, self.published_at) #irá ser sobreescrito pela class PostAdmin em admin.py

#video 3h50
@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):
   #se false, ou seja, não tem slug
   if not instance.slug: 
      instance.slug = slugify(instance.title)
      return instance.save() 

