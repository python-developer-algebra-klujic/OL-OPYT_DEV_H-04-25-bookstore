from django.views.generic import DetailView

from bookstore.models.publishers import Publisher


class PublisherDetailView(DetailView):
    model = Publisher
