# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

from .views import Home, PeopleDetail, PeopleList


urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^person/$', PeopleList.as_view(), name='person_list'),
    url(r'^person/(?P<pk>\d)/$', PeopleDetail.as_view(), name='person_detail'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
