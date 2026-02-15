from celery import shared_task


@shared_task
def hello_celery():
    """Sample task to verify Celery worker is running."""
    return "ok"
