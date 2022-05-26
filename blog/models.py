from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

   

   class Meta:
      ordering = ('-published_at',)#irá mostrar os mais recentes antes

   def __str__(self):
      return "{} - {}".format(self.title, self.published_at) #irá ser sobreescrito pela class PostAdmin em admin.py




