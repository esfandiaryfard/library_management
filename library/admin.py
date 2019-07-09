from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from library.models import Writer

admin.site.unregister(Group)

"""
Customize panel admin for writer managements
"""
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (_('username'), _('password'))}),

        (_('Personal info'), {'fields': (_('name'), _('last_name'), _('national_id'), _('book'))}),

    )
admin.site.register(Writer, UserAdmin)
