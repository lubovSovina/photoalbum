from django.urls import path, include

from .views import UserByToken

urlpatterns = [
    path('user/by/token/', UserByToken.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
]
