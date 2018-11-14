# -*- coding: utf-8 -*-

from django.utils.translation import gettext as _
from django.views.generic import DetailView, ListView, TemplateView

from .models import Person


class Home(TemplateView):
    template_name = 'i18n/home.html'


class PeopleList(ListView):
    queryset = Person.objects.all()


class PeopleDetail(DetailView):
    queryset = Person.objects.all()

    def get_context_data(self, **kwargs):
        person = self.get_object()
        data = super(PeopleDetail, self).get_context_data(**kwargs)

        data['description'] = _(
            "{name:s} is a famous {nationality:s} and their favorite "
            "color is {color:s}."
        ).format(
            name=person.name,
            nationality=getattr(person.nationality, 'label', _('Earthling')),
            color=getattr(person.favorite_color, 'name', _('unknown')),
        )
        return data
