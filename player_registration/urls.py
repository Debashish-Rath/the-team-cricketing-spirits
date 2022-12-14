from unicodedata import name
from django.urls import path
from .views import player_register, registration_success

urlpatterns = [
    path('player-registration', player_register, name='register'),
    path('registration-success', registration_success, name='registration_success')
]
