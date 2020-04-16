from django.apps import AppConfig


class APIlendConfig(AppConfig):
    name = 'APIlend'

    def ready(self):
        import APIlend.signals