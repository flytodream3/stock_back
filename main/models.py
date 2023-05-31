from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class AuthorStamp(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('ստեղծող'),
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        _('ստեղծվել է'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('փոփոխվել է'),
        auto_now=True,
        null=True, blank=True
    )

    class Meta:
        abstract = True
