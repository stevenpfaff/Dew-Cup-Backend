from django.urls import path
from teams import views
urlpatterns = [
    path('all/', views.get_all_teams),
    path('', views.user_team),
]