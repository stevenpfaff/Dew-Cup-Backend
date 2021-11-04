from django.urls import path
from players import views
urlpatterns = [
    path('all/', views.get_all_players),
    path('', views.user_player)
]