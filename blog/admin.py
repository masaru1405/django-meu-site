from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'published_at', 'status')
   list_filter = ('author', 'status', 'created_at', 'published_at')
   raw_id_fields = ('author',)#podemos add outro autor para um mesmo Post (colocamos o id)
   date_hierarchy = 'published_at' #irá mostrar uma navegação com as datas
   search_fields = ('title', 'content')
   prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)
