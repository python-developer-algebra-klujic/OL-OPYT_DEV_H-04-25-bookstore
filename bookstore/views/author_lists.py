from django.views.generic import ListView

from bookstore.models.authors import Author


class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
