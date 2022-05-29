from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
   email = forms.EmailField(required=True, help_text="Required field. Please, type a valid email.")

   class Meta:
      model = User
      fields = ['username', 'email']
   
   #O email utilizado para cadastro deverá ser único
   def clean_email(self):
      email = self.cleaned_data.get("email")
      if User.objects.filter(email=email).exists():
         raise forms.ValidationError("This email is already registered. Please use another.")
      return email