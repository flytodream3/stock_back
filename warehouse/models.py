from django.db import models
from django.utils.translation import gettext_lazy as _

from main.models import AuthorStamp


class StockRoom(AuthorStamp):
    name = models.CharField(
        _('անվանում'),
        max_length=25
    )

    class Meta:
        verbose_name = _('պահեստախուց')
        verbose_name_plural = _('պահեստախցեր')

    def __str__(self):
        return self.name
