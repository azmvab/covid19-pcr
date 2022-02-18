from django.conf.urls import url

from .views import PeopleDetailView, PeopleImageView


urlpatterns = [
    url(r'^(?P<slug>[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?4[0-9a-fA-F]{3}-?[89abAB][0-9a-fA-F]{3}-?[0-9a-fA-F]{12})$', PeopleDetailView.as_view(), name='people-detail'),
    url(r'^(?P<slug>[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?4[0-9a-fA-F]{3}-?[89abAB][0-9a-fA-F]{3}-?[0-9a-fA-F]{12})/image$', PeopleImageView.as_view(), name='people-detail-img')
]
