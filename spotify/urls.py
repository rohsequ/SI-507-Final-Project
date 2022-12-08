from django.urls import path
from .views import AuthURL, spotify_callback, IsAuthenticated


urlpatterns = [
    path('get-auth-url/', AuthURL.as_view()),
    path('spotify-redirect/', spotify_callback),
    path('spotify-is-auth/', IsAuthenticated.as_view())
]