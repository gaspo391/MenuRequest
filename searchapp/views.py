from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import get_user_model
from groupapp.models import Group, GroupMember
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

def search_user(request):
    users = None
    query = None
    group = None
    group_member = []
    if 'q' in request.GET:
        query = request.GET.get('q')
        users = User.objects.all().filter(username__contains=query)
        try:
          group = Group.objects.get(owner=request.user)
          # group_member = GroupMember.objects.filter(group=group)
        except Group.DoesNotExist:
          group = None
        try:
          group_member = list(GroupMember.objects.filter(group=group).values_list('member', flat=True))
        except ObjectDoesNotExist:
          pass
    return render(request, 'search/search_user.html', {'query': query, 'users': users, 'group_member':group_member})