from django.contrib import admin
from django.urls import path, include
from .views import CustomUserCreate, ProfileList ,ProfileDetail

app_name = "users"

urlpatterns = [
    path('register/', CustomUserCreate.as_view()),
    path('profiles/', ProfileList.as_view()),
    path('profiles/<int:pk>', ProfileDetail.as_view()),
    # path('logout/blacklist/', BlackListTokenView.as_view(),name="blacklist"),
]
