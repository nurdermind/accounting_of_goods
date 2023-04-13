from celery import shared_task

from django.core.mail import mail_admins, EmailMessage
from django.conf import settings
from report_generation import ModelReport


@shared_task
def send_model_report(old_instance, new_instance, lookup_fields, report_format):
    report = ModelReport(report_format=report_format,
                         old_instance=old_instance,
                         new_instance=new_instance,
                         lookup_fields=lookup_fields,
                         )
    report_path = report.generate()
    print(report_path)
    mail = EmailMessage(
        'Stock changes',
        report.title,
        settings.SERVER_EMAIL, [email for name, email in settings.ADMINS])
    mail.attach_file(report_path)
    mail.send(fail_silently=False)
