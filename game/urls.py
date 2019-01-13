from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('board.html', views.board, name='board'),
]