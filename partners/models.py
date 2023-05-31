from django.db import models
from django.utils.translation import gettext_lazy as _

from main.models import AuthorStamp


class Division(AuthorStamp):
    code = models.CharField(
        _('Կոդ'),
        max_length=255
    )
    name = models.CharField(
        _('Անվանում'),
        max_length=255
    )
    contact = models.CharField(
        _('Կոնտակտ'),
        max_length=255,
        blank=True, null=True
    )
    phone = models.CharField(
        _('Հեռախոս'),
        max_length=15,
        blank=True, null=True
    )

    class Meta:
        verbose_name = _('Ստորաբաժանում')
        verbose_name_plural = _('Ստորաբաժանումներ')

    def __str__(self):
        return '%s %s' % (self.code, self.name)
