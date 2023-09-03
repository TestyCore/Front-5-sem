from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # primary key field type int
    name = 'administrator'  # app name
