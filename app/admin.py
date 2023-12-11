from django.contrib import admin
from .models import UserAccount
from .models import Guest

class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'email', 'date_joined', 'is_active_display')
    list_filter = ('is_active',)  

    def is_active_display(self, obj):
        return obj.is_active

    is_active_display.boolean = True
    is_active_display.short_description = 'Is Active' 

class GuestAdmin(admin.ModelAdmin):
    list_display = ('ip_address','visit_counter')



admin.site.register(UserAccount,UserAdmin)
admin.site.register(Guest,GuestAdmin)
