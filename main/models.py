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
    deleted_at = models.DateTimeField(
        _('ջնջվել է'),
        null=True, blank=True
    )
    deleted = models.BooleanField(
        _('ջնջված'),
        default=False
    )

    class Meta:
        abstract = True


class Category(AuthorStamp):
    name = models.CharField(
        _('անվանում'),
        max_length=255
    )
    icon = models.ImageField(
        _('պատկեր'),
        upload_to='images/categories/icons/',
        default='images/no_image.png',
        blank=True, null=True
    )

    class Meta:
        verbose_name = _('Դասակարգ')
        verbose_name_plural = _('Դասակարգեր')

    def __str__(self):
        return self.name


class SubCategory(AuthorStamp):
    category = models.ForeignKey(
        Category,
        verbose_name=_('դասակարգ'),
        on_delete=models.CASCADE
    )
    name = models.CharField(
        _('անվանում'),
        max_length=255
    )
    icon = models.ImageField(
        _('պատկեր'),
        upload_to='images/subcategories/icons/',
        default='images/no_image.png',
        blank=True, null=True
    )

    class Meta:
        verbose_name = _('Ենթադասակարգ')
        verbose_name_plural = _('Ենթադասակարգեր')

    def __str__(self):
        return self.name
