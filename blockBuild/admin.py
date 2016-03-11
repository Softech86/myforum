from django.contrib import admin

# Register your models here.
from models import UserData

class UserAdmin(admin.ModelAdmin):
    #list_display = ('userName', 'userDesc', 'author', 'create_timestamp', 'last_update_timestamp', )
    #list_filter = ('author', )
    pass

admin.site.register(UserData)#, UserAdmin)
