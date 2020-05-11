from django.contrib import admin
from django.urls import path
from .views import menufunc, MenuDetail, MenuCreate, MenuDelete, MenuRequest, menu_list

app_name='menuapp'

urlpatterns = [
    path('', menufunc, name='menu'),
    # path('list/', MenuList.as_view(), name="list"),
    path('list/', menu_list, name="list"),
    path('detail/<int:pk>', MenuDetail.as_view(), name='detail'),
    path('create/', MenuCreate.as_view(), name='create'),
    path('delete/<int:pk>', MenuDelete.as_view(), name="delete"),
    path('menurequest/', MenuRequest.as_view(), name='menurequest'),
]
