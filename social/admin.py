from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
   readonly_fields = ['created_at', 'modified_at']
   list_display = ['social_network', 'description', 'modified_at']