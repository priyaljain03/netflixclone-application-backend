from django.contrib import admin
from django.urls import path, include,re_path
from .views import MoviesList, MovieDetail , VideoList

urlpatterns = [
    re_path(r'^movies/$', MoviesList.as_view()),
    path('movie/<int:pk>/', MovieDetail.as_view()),
]
