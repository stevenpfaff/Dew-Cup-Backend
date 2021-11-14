from django.urls import path
from tournament import views
urlpatterns = [
    path('all/', views.get_tourney),
    path('', views.user_tourney),
]