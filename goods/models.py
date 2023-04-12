from django.db import models
from django.utils.translation import gettext_lazy as _


class Good(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Навзание'))
    description = models.TextField(verbose_name=_('Описание'), blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('Цена'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    stock = models.PositiveIntegerField(default=0, verbose_name=_('Остаток'))

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
