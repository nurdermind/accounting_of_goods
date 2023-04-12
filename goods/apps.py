from django.apps import AppConfig
from django.core.signals import request_finished


class GoodsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "goods"

    def ready(self):
        from . import signals
        request_finished.connect(signals.good_stock_update_handler, dispatch_uid="good_stock_update_handler")
