from celery import shared_task
from django.core.management import call_command  # NEW


@shared_task
def sample_task():
    print("The sample task just ran.")
