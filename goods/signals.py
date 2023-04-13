from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Good
from .tasks import send_model_report
from django.conf import settings

from loguru import logger


@receiver(pre_save, sender=Good)
def good_stock_update_handler(sender, **kwargs):
    good = kwargs.get('instance')

    if good and good.pk is not None:

        previous_good = Good.objects.get(pk=good.pk)
        if previous_good.stock != good.stock:
            send_model_report(old_instance=previous_good, new_instance=good, lookup_fields=['stock'],
                              report_format=settings.REPORT_FORMAT)
