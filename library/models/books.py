from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

"""
Create model Book
"""


class Book(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('name'), null=True)
    ISBN = models.CharField(max_length=256, verbose_name=_('last name'), null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('book')
        app_label = "library"
        db_table = "books"

    @staticmethod
    def get_books():
        return Book.objects.all()

    def __str__(self):
        return self.name