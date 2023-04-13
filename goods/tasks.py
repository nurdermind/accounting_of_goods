from celery import shared_task
from loguru import logger

from .models import Good
from .report_generation import ModelReport


@shared_task
def send_model_report(old_instance, new_instance, lookup_fields, report_format):
    report_path = ModelReport(report_format=report_format,
                              old_instance=old_instance,
                              new_instance=new_instance,
                              lookup_fields=lookup_fields,
                              ).generate()

