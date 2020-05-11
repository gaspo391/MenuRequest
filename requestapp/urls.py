from django.urls import path
from . import views

app_name='requestapp'

urlpatterns = [
    path('add/<int:menu_id>/', views.add_requests, name='add_requests'),
    path('', views.requests, name='requests'),
    path('cancel/<int:menu_id>/', views.request_cancel, name='request_cancel'),
    path('cancel_send_request/', views.cancel_send_request, name='cancel_send_request'),
    path('send_request/', views.send_request, name='send_request'),
    path('receive_list/<int:requests_id>', views.receive_list, name='receive_list'),
    path('answer_request/<int:request_menu_id>', views.answer_request, name='answer_request'),
    path('request_clear/', views.request_clear, name='request_clear'),
]