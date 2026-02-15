"""
Test settings: SQLite in-memory DB, Celery eager (no broker).
Use by setting DJANGO_SETTINGS_MODULE=opc.settings_test or via pytest.
"""
from opc.settings import *  # noqa: F401, F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Run Celery tasks synchronously in tests
CELERY_TASK_ALWAYS_EAGER = True
