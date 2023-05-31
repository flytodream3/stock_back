from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class StockUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Username must be set.')
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_staff = True
        user.is_manager = True
        user.is_stock_user = False
        user.is_superuser = True
        user.save(using=self._db)
        return user


class StockUser(AbstractUser):
    is_manager = models.BooleanField(default=False, verbose_name=_('Manager'))
    is_stock_user = models.BooleanField(default=True, verbose_name=_('Stock User'))
    phone = models.CharField(
        _('Phone Number'),
        max_length=50,
        null=True, blank=True
    )

    objects = StockUserManager()

    class Meta:
        verbose_name = _('Օգտատեր')
        verbose_name_plural = _('Օգտատերեր')


class Profile(models.Model):
    user = models.OneToOneField(
        StockUser,
        verbose_name=_('Owner'),
        on_delete=models.CASCADE
    )
    pic = models.ImageField(
        upload_to='users/profile/',
        default='users/none.png',
        blank=True, null=True
    )
    address = models.CharField(
        _('Address'),
        max_length=255,
        null=True, blank=True
    )
    city = models.CharField(
        _('City'),
        max_length=255,
        null=True, blank=True
    )
    state = models.CharField(
        _('state/province'),
        max_length=255,
        null=True, blank=True
    )
    country = models.CharField(
        _('country'),
        max_length=255,
        null=True, blank=True
    )
    document = models.FileField(
        _('document'),
        upload_to='users/profile/docs',
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('updated at'),
        auto_now=True
    )

    class Meta:
        verbose_name = _('անձնական էջ')
        verbose_name_plural = _('անձնական էջեր')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=StockUser)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=StockUser)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
