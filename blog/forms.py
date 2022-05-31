from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = '__all__'
      widgets = {
         'content': forms.CharField(widget=CKEditorWidget())
      }