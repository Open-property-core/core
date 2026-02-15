from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "opc.apps.notifications"
    verbose_name = "Notifications"

    def ready(self):
        import opc.apps.notifications.signals  # noqa: F401
