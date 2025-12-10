from django.views.generic import DetailView

from bookstore.models.books import Book


class BookDetailView(DetailView):
    model = Book
