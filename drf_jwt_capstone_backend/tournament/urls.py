from django.urls import path
from tournament import views
urlpatterns = [
    path('all/', views.get_tourney),
    path('<str:name>/', views.single_tourney),
    path('', views.create_tourney),
]