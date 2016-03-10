from django.contrib import admin

# Register your models here.
from models import UserData

class UserAdmin(admin.ModelAdmin):
    list_display = ('userName', 'userSex', 'last_update_timestamp')
    list_filter = ('userSex', )
admin.site.register(UserData, UserAdmin)
