from django.views.generic import DetailView

from bookstore.models.authors import Author


class AuthorDetailView(DetailView):
    model = Author
