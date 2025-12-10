from django.views.generic import ListView

from bookstore.models.publishers import Publisher


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publisher_list'
