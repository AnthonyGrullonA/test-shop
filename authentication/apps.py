from django.apps import AppConfig
from django.db.models.signals import post_migrate

def run_initialization_script(sender, **kwargs):
    import scripts.initialization_script
    scripts.initialization_script.run()
class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    def ready(self):
        post_migrate.connect(run_initialization_script, sender=self)