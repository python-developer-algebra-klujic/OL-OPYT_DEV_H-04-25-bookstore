from django.views.generic import ListView

from bookstore.models.books import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
