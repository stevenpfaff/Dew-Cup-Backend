from django.urls import path
from games import views
urlpatterns = [
    path('all/', views.get_all_games),
    path('<str:game>/', views.tourney_game),
    path('single/<int:games_pk>/', views.single_game),
    path('', views.create_game),
]