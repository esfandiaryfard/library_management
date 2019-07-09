from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from .books import Book
from django.contrib.auth.models import AbstractUser


"""
Create model Writer, this model is an override of model user in django, but with added field based on requirements
"""
class Writer(AbstractUser):
    book = models.ForeignKey(Book, related_name='books', blank=False, verbose_name=_('book'),
                                on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=256, verbose_name=_('name'), null=True)
    last_name = models.CharField(max_length=256, verbose_name=_('last name'), null=True)
    national_id = models.PositiveIntegerField(unique=True, verbose_name=_('national id'), null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('writer')
        app_label = "library"
        db_table = "writers"
