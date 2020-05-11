from django.urls import path, include
from . import views

app_name='searchapp'

urlpatterns = [
    path('search_user/', views.search_user, name='search_user'),
]
