from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'published_at', 'status')
   list_filter = ('author', 'status', 'created_at', 'published_at')
   raw_id_fields = ('author',)#podemos add outro autor para um mesmo Post (colocamos o id)
   date_hierarchy = 'published_at' #irá mostrar uma navegação com as datas
   search_fields = ('title', 'content')
   prepopulated_fields = {'slug':('title',)} #ao digita o title no painel admin, já preenche o campo slug
   readonly_fields = ('show_image',) #6h25m

   #6h25m
   #para mudar o label da propriedade 'view_image' no admin
   def show_image(self, obj):
      return obj.view_image
   show_image.short_description = "Imagem cadastrada"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('category_type',)
   list_filter = ('category_type',)
   date_hierarchy = 'published_at'
   search_fields = ('category_type',)

#admin.site.register(Post, PostAdmin, Category, CategoryAdmin)
