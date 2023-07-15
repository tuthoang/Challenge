from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.ImageSearchListView.as_view(), name='search-list-url'),
]
