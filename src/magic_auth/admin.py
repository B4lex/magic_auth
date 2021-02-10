from django.contrib import admin

from magic_auth.models import MagicUser


class MagicUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'has_access')


admin.site.register(MagicUser, MagicUserAdmin)
