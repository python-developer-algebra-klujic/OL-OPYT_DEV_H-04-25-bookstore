from django.contrib import admin

from .models.authors import Author
from .models.books import Book
from .models.publishers import Publisher


admin.site.register([Publisher, Author, Book])
