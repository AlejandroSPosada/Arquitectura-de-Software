from django.apps import AppConfig
from django.utils.module_loading import import_string
from django.conf import settings

class PagesConfig(AppConfig):  # <-- antes decía PageConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

    def ready(self):
        ImageStorageClass = import_string(settings.IMAGE_STORAGE_CLASS)