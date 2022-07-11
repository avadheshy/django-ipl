
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('played', views.played),
    path('won', views.won),
    path('runs', views.runs),
    path('bowler', views.bowler),
]
