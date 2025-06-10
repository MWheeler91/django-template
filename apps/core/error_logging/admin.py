from django.contrib import admin
from .models import *
from utils.admin import BaseModelAdmin
# from utils.discord_bot import send_discord_dm
from apps.core.account.models import User
import environ

# Register your models here.
admin.site.register(Error)
admin.site.register(StackTrace)

env = environ.Env()

# class ErrorAdmin(BaseModelAdmin):
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)

#         user = User.objects.get(id=1)
#         bot_key = env('ERROR_BOT_TOKEN')
#         msg = f'{obj.error_type} EXCEPTION \n App: {obj.app}\nFile: {obj.file}.{obj.funct}\n{obj.error} '

#         send_discord_dm(bot_key, user.discord_user_id, msg)

        
        