from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PeopleConfig(AppConfig):
    name = 'apps.people'
    verbose_name = _("People")
