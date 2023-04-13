from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Good(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('Price'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of created'))
    stock = models.PositiveIntegerField(default=0, verbose_name=_('Stock'), validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = _('Good')
        verbose_name_plural = _('Goods')
