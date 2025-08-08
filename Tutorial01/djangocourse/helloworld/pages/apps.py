from django.apps import AppConfig

class PagesConfig(AppConfig):  # <-- antes decía PageConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
