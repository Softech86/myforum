from django.contrib import admin

# Register your models here.

from models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('block', 'author', 'title', 'content', 'status', 'create_timestamp', 'last_update_timestamp')
    list_filter = ('block', )
    search_fields = ['title', 'content']
    
admin.site.register(Article, ArticleAdmin)
