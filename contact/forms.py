from django import forms

#7h48m
class ContactForm(forms.Form):
   name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder':'Digite seu nome'}))
   email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder':'Digite seu melhor email'}))
   message = forms.CharField(label="Mensagem", widget=forms.Textarea(attrs={'placeholder':'Digite sua mensagem'}))