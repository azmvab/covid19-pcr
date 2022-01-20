from django.conf.urls import url

from .views import PeopleDetailView


urlpatterns = [
    url(r'^(?P<guid>[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?4[0-9a-fA-F]{3}-?[89abAB][0-9a-fA-F]{3}-?[0-9a-fA-F]{12})$', PeopleDetailView.as_view(), name='people-detail')
]
