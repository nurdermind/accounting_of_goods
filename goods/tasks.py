from celery import shared_task

from django.core.mail import send_mail
from report_generation import ModelReport


@shared_task
def send_model_report(old_instance, new_instance, lookup_fields, report_format):
    report = ModelReport(report_format=report_format,
                              old_instance=old_instance,
                              new_instance=new_instance,
                              lookup_fields=lookup_fields,
                              )
    report_path = report.generate()

    # send_mail(
    #     'Stock changes',
    #     report.title,
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )
