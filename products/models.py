from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from warehouse.models import StockRoom
from main.models import AuthorStamp


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


class Measure(AuthorStamp):
    name = models.CharField(
        _('անվանում'),
        max_length=255
    )

    class Meta:
        verbose_name = _('Չափման միավոր')
        verbose_name_plural = _('Չափման միավորներ')

    def __str__(self):
        return self.name


class Product(AuthorStamp):
    category = models.ForeignKey(
        Category,
        verbose_name=_('Դասակարգ'),
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    subcategory = models.ForeignKey(
        SubCategory,
        verbose_name=_('Ենթադասակարգ'),
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    as_key = models.CharField(
        _('ՀԾ Կոդ'),
        max_length=30,
        null=True, blank=True
    )
    p_num = models.CharField(
        _('Գործարանային համար'),
        max_length=50,
        null=True, blank=True
    )
    name = models.CharField(
        _('Անվանում'),
        max_length=300
    )
    image = models.ImageField(
        _('Նկար'),
        upload_to='images/products/',
        default='images/no_image.png',
        blank=True, null=True
    )
    stockroom = models.ForeignKey(
        StockRoom,
        verbose_name=_('պահեստախուց'),
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    quantity = models.DecimalField(
        _('Քանակ'),
        max_digits=10,
        decimal_places=3,
        default=0
    )
    out_count = models.DecimalField(
        _('Ընդամենը դուրսգրված քանակ'),
        max_digits=10,
        decimal_places=3,
        default=0,
        editable=False
    )
    count = models.PositiveIntegerField(
        _('Ընդամենը ելքերի քանակ'),
        default=0,
        editable=False
    )
    measure = models.ForeignKey(
        Measure,
        verbose_name=_('Չ/Մ'),
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    critical_quantity = models.DecimalField(
        _('Մինիմալ քանակ'),
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True,
        default=None
    )
    is_active = models.BooleanField(
        _('Առկայություն'),
        default=True
    )
    in_use = models.BooleanField(
        _('Օգտագործման մեջ է'),
        default=False
    )
    description = models.TextField(
        _('Նկարագրություն'),
        null=True, blank=True
    )

    class Meta:
        verbose_name = _('Ապրանք')
        verbose_name_plural = _('Ապրանքներ')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.quantity <= 0:
            self.is_active = False
        else:
            self.is_active = True

        super().save(*args, **kwargs)


