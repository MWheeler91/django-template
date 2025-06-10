from django.contrib import admin
from .models import *
from utils.admin import BaseModelAdmin


# Register your models here.
class DefaultAdmin(BaseModelAdmin):
    pass

# class Admin(admin.ModelAdmin):
#     pass
