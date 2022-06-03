from django.shortcuts import render
from .forms import ContactForm

#7h36m
def contact(request):
   send = False
   form = ContactForm(request.POST or None)
   if form.is_valid():
      send = True
   
   context = {
      'form': form,
      'success': send
   }
   return render(request, 'contact/contact.html', context)