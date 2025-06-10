from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

class BaseModel(models.Model):
    entered_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name='%(class)s_entered_by'
    )
    date_entered = models.DateField(default=datetime.now)
    last_updated_date = models.DateField(auto_now=True, blank=True, null=True)
    last_updated_time = models.TimeField(auto_now=True, blank=True, null=True)
    last_updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name='%(class)s_updated_by'
    )

    class Meta:
        abstract = True


class CommonModel(models.Model):
    name = models.CharField(max_length=255)
    app_label = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        unique_together = ('name', 'app_label')
        ordering = ['app_label', 'name']

    def __str__(self):
        return f"{self.name} ({self.app_label})"
