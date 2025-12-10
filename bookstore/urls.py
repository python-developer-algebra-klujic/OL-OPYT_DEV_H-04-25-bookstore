from django.urls import path

from .views import (PublisherListView,
                    PublisherDetailView)


urlpatterns = [
    path('', PublisherListView.as_view()),
    path('<int:pk>/', PublisherDetailView.as_view())
]
