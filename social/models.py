from django.db import models

#7h08m
class Link(models.Model):
   social_network = models.SlugField(verbose_name="Identificação Rede", max_length=100, unique=True)
   description = models.CharField(verbose_name="Descrição", max_length=100)
   url = models.URLField(max_length=200, null=False, blank=False)
   created_at = models.DateTimeField(auto_now_add=True)#só irá add a data na 1ª vez | campo oculto
   modified_at = models.DateTimeField(auto_now=True)#campo oculto

   class Meta:
      verbose_name = "Link"
      verbose_name_plural = "Links"
      ordering = ["social_network"]
   
   def __str__(self):
      return self.social_network