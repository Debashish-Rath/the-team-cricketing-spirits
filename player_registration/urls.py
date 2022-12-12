from unicodedata import name
from django.urls import path
from .views import player_register

urlpatterns = [
    path('player-registration', player_register, name='register')
]
