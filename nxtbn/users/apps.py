from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'nxtbn.users'

    def ready(self):
        import nxtbn.users.signals  # noqa
