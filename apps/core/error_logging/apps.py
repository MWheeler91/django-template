from django.apps import AppConfig


class ErrorLoggingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core.error_logging'
    verbose_name = 'Error Logs'
