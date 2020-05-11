from django.urls import path
from . import views

app_name='groupapp'

urlpatterns = [
    path('make_group/', views.make_group, name='make_group'),
    path('delete_group/', views.delete_group, name='delete_group'),
    path('invitate_group/<int:user_id>', views.invitate_group, name='invitate_group'),
    path('add_member/<int:user_id>', views.add_member, name='add_member'),
    path('remove_member/<int:user_id>', views.remove_member, name='remove_member'),
    path('member_list/', views.member_list, name='member_list'),
    path('invitated_list/', views.invitated_list, name='invitated_list'),
    path('participate_group/<int:group_id>', views.participate_group, name='participate_group'),
    # path('register_member/', views.register_member, name='register_member'),
    # path('send_request/<int:requests_id>', views.send_request, name='send_request'),
]
