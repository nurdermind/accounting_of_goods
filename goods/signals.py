from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Good
from .tasks import generate__and__send_stock_report

from loguru import logger


@receiver(pre_save, sender=Good)
def good_stock_update_handler(sender, **kwargs):

    good = kwargs.get('instance')

    if good and good.pk is not None:

        previous_good = Good.objects.get(pk=good.pk)
        if previous_good.stock != good.stock:
            generate__and__send_stock_report(good)
