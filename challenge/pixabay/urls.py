from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.ImageSearchListView.as_view(), name='search-list-url'),
    path("detail/<int:pk>/", views.ImageDetailView.as_view(), name='image-detail-url'),
]
