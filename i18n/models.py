# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import override, ugettext_lazy as _

from parler.models import TranslatedFields, TranslatableModel


class Color(TranslatableModel):
    code = models.CharField(
        blank=False,
        default='',
        help_text=_('Please provide an internal code for this color.'),
        max_length=32,
        unique=True,
        verbose_name=_('code'),
    )
    translations = TranslatedFields(
        name=models.CharField(blank=False,
                              default='',
                              help_text=_('Please provide a name for this color.'),
                              max_length=32,
                              verbose_name=_('name')),
    )

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')

    def __str__(self):
        return self.code


class Nationality(TranslatableModel):
    country_code = models.CharField(
        blank=False,
        default='',
        help_text=_('Please provide the ISO 2-letter country-code for this nationality.'),
        max_length=2,
        unique=True,
        verbose_name=_('country code'),
    )
    translations = TranslatedFields(
        label=models.CharField(blank=False,
                               default='',
                               help_text=_('Please provide a label for this nationality.'),
                               max_length=32,
                               verbose_name=_('label')),
    )

    class Meta:
        verbose_name = _('nationality')
        verbose_name_plural = _('nationalities')

    def __str__(self):
        return self.country_code


class Person(models.Model):
    name = models.CharField(
        blank=False,
        default='',
        help_text=_('Please provide a name.'),
        max_length=32,
        verbose_name=_('name')
    )

    nationality = models.ForeignKey(
        to='i18n.Nationality',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('nationality')
    )

    favorite_color = models.ForeignKey(
        to='i18n.Color',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('favorite color'),
    )

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')

    def __str__(self):
        return self.name

    def get_absolute_url(self, language_code=None):
        """
        Returns the URL for this person in the current language.
        """
        if language_code:
            with override(language_code):
                return reverse('person_detail', kwargs={'pk': self.pk})
        else:
            return reverse('person_detail', kwargs={'pk': self.pk})
