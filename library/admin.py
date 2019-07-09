from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from library.models import Writer
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(Group)

"""
Customize panel admin for writer managements
"""


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': (_('username'))}),

        (_('Personal info'), {'fields': (_('name'), _('last_name'), _('national_id'), _('book'))}),

    )
admin.site.register(Writer, UserAdmin)
