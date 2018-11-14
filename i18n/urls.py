"""i18n URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
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
