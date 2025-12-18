from django.urls import reverse_lazy
from django.views.generic import CreateView

from bookstore.models.authors import Author


class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'

    success_url = reverse_lazy('author_create')
