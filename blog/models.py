from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = [('draft', 'Draft'), ('published', 'Published')]

class Post(models.Model):
   title = models.CharField(max_length=200)
   slug = models.SlugField(max_length=200)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   content = models.TextField()
   published_at = models.DateTimeField(default=timezone.now)
   created_at = models.DateTimeField(auto_now_add=True)#só irá add a data na 1ª vez | campo oculto
   modified_at = models.DateTimeField(auto_now=True)#campo oculto
   status = models.CharField(max_length=20, choices=STATUS, default='draft')

   class Meta:
      ordering = ('-published_at',)

   def __str__(self):
      return "{} - {}".format(self.title, self.published_at)

