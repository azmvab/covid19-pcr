"""
travel URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .views import Index

SITE_NAME = "Travel"

admin.site.site_title = _('%s administration' % SITE_NAME)
admin.site.site_header = _('%s site administration' % SITE_NAME)
admin.site.index_title = _('Site administration')

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^people/', include(('apps.people.urls', 'people'))),

]
