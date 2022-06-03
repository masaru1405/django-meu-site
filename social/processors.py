from .models import Link

#7h27
def context_social(request):
   context_dict = {}
   links = Link.objects.all()
   for i in links:
      context_dict[i.social_network] = i.url
   return context_dict