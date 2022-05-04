from django.urls import path, include
from .views import GetListAllPhoto, ItemPhotoViews, ListPhotosByUsers, CreatePhoto

urlpatterns = [
    path('list/all/photo/', GetListAllPhoto.as_view()),
    path('create/photo/', CreatePhoto.as_view()),
    path('item/photo/<int:pk>/', ItemPhotoViews.as_view()),
    path('list/photo/user/<int:pk>/', ListPhotosByUsers.as_view()),
]