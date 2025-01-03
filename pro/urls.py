from django.urls import path

from pro import views
from . import views

urlpatterns = [
    path('', views.game_page, name='game_page'), 
    path('start_game', views.start_game, name='start_game'),
    path('move_snake', views.move_snake, name='move_snake'),
]



















# urlpatterns = [
#     path('',views.home)
# ]
