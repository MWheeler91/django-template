from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

User = get_user_model()

class BaseModelAdmin(admin.ModelAdmin):
    base_readonly_fields = (
        'id',
        'entered_by',
        'date_entered',
        'last_updated_date',
        'last_updated_time',
        'last_updated_by',
     )
    def get_readonly_fields(self, request, obj=None):
        valid_fields = []
        model = self.model
        for field in self.base_readonly_fields:
            if (
                hasattr(model, field) or
                hasattr(self, field)
            ):
                valid_fields.append(field)
        return valid_fields + list(super().get_readonly_fields(request, obj))

    def get_list_display(self, request):
        default_list_display = super().get_list_display(request)
        if 'id' not in default_list_display:
            return ('id',) + tuple(default_list_display)
        return default_list_display

    def get_system_user(self):
        return User.objects.get(username="sys")

    def save_model(self, request, obj, form, change):
        user = request.user
        if isinstance(user, AnonymousUser) or not user.is_authenticated:
            user = self.get_system_user()

        if not change and not obj.entered_by:
            obj.entered_by = user
        obj.last_updated_by = user

        super().save_model(request, obj, form, change)
