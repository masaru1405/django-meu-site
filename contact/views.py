from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm

#7h36m
def contact(request):
   send = False
   form = ContactForm(request.POST or None)
   if form.is_valid(): 
      name = request.POST.get('name', '') #7h57
      email = request.POST.get('email', '')
      message = request.POST.get('message', '')
      send_email = EmailMessage(
         "Mensagem do Blog Django",
         "De {} <{}> \n\nEscreveu: \n{}".format(name, email, message),
         "do-not-reply@inbox.mailtrap.io",
         ["kmn1405.cd@gmail.com"],
         reply_to=[email]
      )
      try:
         send_email.send()
         send = True
      except:
         send = False
   
   context = {
      'form': form,
      'success': send
   }
   return render(request, 'contact/contact.html', context)