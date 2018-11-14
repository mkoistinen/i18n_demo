# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms import widgets
from django.utils.translation import force_text, get_language


class AllTranslationsMixin(object):
    """
    'Stolen' from https://github.com/aldryn/aldryn-translation-tools/
    Written here by the same author (mkoistinen) but adapted here to not
    depend on Django CMS.
    """
    @property
    def media(self):
        return super(AllTranslationsMixin, self).media + widgets.Media(
            css={'all': ('css/admin/all-translations-mixin.css', ), }
        )

    def all_translations(self, obj):
        """
        Adds a property to the list_display that lists all translations with
        links directly to their change forms. Includes CSS to style the links
        to looks like tags with color indicating current language, active and
        inactive translations.

        A similar capability is in HVAD, and now there is this for
        Parler-based projects.
        """
        available = list(obj.get_available_languages())
        current = get_language()
        langs = []
        for code, lang_name in settings.LANGUAGES:
            classes = ["lang-code", ]
            title = force_text(lang_name)
            if code == current:
                classes += ["current", ]
            if code in available:
                classes += ["active", ]
                title += " (translated)"
            else:
                title += " (untranslated)"
            change_form_url = reverse(
                'admin:{app_label}_{model_name}_change'.format(
                    app_label=obj._meta.app_label.lower(),
                    model_name=obj.__class__.__name__.lower(),
                ), args=(obj.id, ))
            link = (
                '<a class="{classes}" href="{url}?language={code}" '
                'title="{title}">{code}</a>'
            ).format(
                classes=' '.join(classes),
                url=change_form_url,
                code=code,
                title=title,
            )
            langs.append(link)
        return ''.join(langs)
    all_translations.short_description = 'Translations'
    all_translations.allow_tags = True

    def get_list_display(self, request):
        """
        Unless the the developer has already placed "all_translations" in the
        list_display list (presumably specifically where she wants it), append
        the list of translations to the end.
        """
        list_display = super().get_list_display(request)
        if 'all_translations' not in list_display:
            list_display = list(list_display) + ['all_translations', ]
        return list_display
