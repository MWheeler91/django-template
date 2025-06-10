from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class AdminUser(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email',)
    ordering = ('id','email',)
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = UserAdmin.add_fieldsets
    # add_fieldsets = (
    #         (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
    #     )

    
admin.site.register(User, AdminUser)
