from django.urls import path

from .views import (PublisherListView,
                    PublisherDetailView,
                    BookListView,
                    BookDetailView,
                    AuthorDetailView,
                    AuthorListView,
                    AuthorCreateView)


urlpatterns = [
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher_details'),

    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_details'),

    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_details'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create')
]
