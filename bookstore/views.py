from django.views.generic import ListView, DetailView

from .models.publishers import Publisher


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publisher_list'


class PublisherDetailView(DetailView):
    model = Publisher
