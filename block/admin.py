from django.contrib import admin

# Register your models here.

from models import Block

class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'author', 'create_timestamp', 'last_update_timestamp', )
    list_filter = ('author', )

admin.site.register(Block, BlockAdmin)
