from celery import shared_task
from loguru import logger

from .models import Good


@shared_task
def generate__and__send_stock_report(good: Good):
    logger.info("Generating report for good {}".format(good))
