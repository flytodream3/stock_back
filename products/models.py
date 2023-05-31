from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from warehouse.models import StockRoom
from main.models import AuthorStamp







