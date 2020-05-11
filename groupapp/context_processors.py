from .models import Group, GroupMember
from requestapp.models import Requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def mygroup(request):
    mygroup = None
    send_request = None
    if request.user.is_authenticated:
        try:
            mygroup = Group.objects.get(owner=request.user)
            try:
                send_request = mygroup.requests
            except Requests.DoesNotExist:
                send_request = None
        except Group.DoesNotExist:
            mygroup = None
    return dict(mygroup=mygroup, send_request=send_request)

def receive_request(request):
    group_member = None
    belong_group = None
    receive_request = None
    if request.user.is_authenticated:
        try:
            group_member = GroupMember.objects.get(member=request.user)
            belong_group = group_member.group
            receive_request = belong_group.requests
        except GroupMember.DoesNotExist:
            receive_request = None
    return dict(receive_request=receive_request)

