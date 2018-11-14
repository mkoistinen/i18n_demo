# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _

from parler.admin import TranslatableAdmin

from .mixins.admin import AllTranslationsMixin

from .models import Color, Nationality, Person


@admin.register(Color)
class ColorAdmin(AllTranslationsMixin, TranslatableAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'name',
            )
        }),
        (_('Advanced'), {
            'classes': ('collapse', ),
            'fields': (
                'code',
            )
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        # The official django-parler workaround for prepopulated_fields.
        # See: https://django-parler.readthedocs.io/en/latest/compatibility.html#using-prepopulated-fields-in-the-admin  # noqa
        return {
            'code': ('name',)
        }


@admin.register(Nationality)
class NationalityAdmin(AllTranslationsMixin, TranslatableAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'label',
            )
        }),
        (_('Advanced'), {
            'classes': ('collapse', ),
            'fields': (
                'country_code',
            )
        }),
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'favorite_color', )
    fieldsets = (
        (None, {
            'fields': ('name', 'nationality', 'favorite_color', )
        }),
    )
