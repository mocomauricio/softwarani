from django.apps import AppConfig


class AssociationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'asociación'
    name = 'apps.association'

    def ready(self):
        import apps.association.signals 