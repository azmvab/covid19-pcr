from django.views import generic
from .models import Person


class PeopleDetailView(generic.DetailView):
    """
    Experiance Detail View
    """
    template_name = 'index.html'
    queryset = Person.objects.all()