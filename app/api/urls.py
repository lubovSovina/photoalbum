from django.urls import path, include

urlpatterns = [
    path('users/', include('api.user.urls')),
    path('photo/', include('api.photo.urls')),
]
