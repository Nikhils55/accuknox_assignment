# accuknox_assignment/apps.py

from django.apps import AppConfig

class AccuknoxAssignmentConfig(AppConfig):
    name = 'accuknox_assignment'

    def ready(self):
        # Import signals here to ensure apps are loaded.
        from . import signals
