from django.urls import path
from teams import views
urlpatterns = [
    path('all/', views.get_all_teams),
    path('<str:name>/', views.user_team),
    path('',views.create_team)
]