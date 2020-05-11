from django.shortcuts import render, redirect, get_object_or_404
from menuapp.models import Menu
from .models import Requests, RequestMenu
from groupapp.models import Group, GroupMember
# from account.models import GroupUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def _requests_id(request):
    requests = request.session.session_key
    if not requests:
        requests = request.session.create()
    return requests

@login_required
def add_requests(request, menu_id):
  menu = Menu.objects.get(id=menu_id)
  try:
      # requests = Requests.objects.get(requests_id=_requests_id(request))
      requests = Requests.objects.get(requests_owner=request.user)
  except Requests.DoesNotExist:
      requests = Requests.objects.create(
              # requests_id =  _requests_id(request)
              requests_owner =  request.user
          )
      requests.save()
  try:
      request_menu = RequestMenu.objects.get(menu=menu, requests=requests)
      request_menu.save()
  except RequestMenu.DoesNotExist:
      request_menu = RequestMenu.objects.create(
              menu = menu,
              requests = requests
          )
      request_menu.save()
  return redirect('menuapp:list')

@login_required
def requests(request):
  request_menu = []
  try:
    # requests = Requests.objects.get(requests_id=_requests_id(request))
    requests = Requests.objects.get(requests_owner=request.user)
    request_menu = RequestMenu.objects.filter(requests=requests, active=True)
  except ObjectDoesNotExist:
    pass

  return render(request, 'requests/requests.html', {'request_menu':request_menu})

@login_required
def receive_list(request, requests_id):
  request_menu = []
  try:
    # requests = Requests.objects.get(requests_id=_requests_id(request))
    requests = Requests.objects.get(id=requests_id)
    request_menu = RequestMenu.objects.filter(requests=requests, active=True)
  except ObjectDoesNotExist:
    pass

  return render(request, 'requests/receive_list.html', {'request_menu':request_menu})

@login_required
def request_cancel(request, menu_id):
  # requests = Requests.objects.get(requests_id=_requests_id(request))
  requests = Requests.objects.get(requests_owner=request.user)
  menu = get_object_or_404(Menu, id=menu_id)
  request_menu = RequestMenu.objects.get(menu=menu, requests=requests)
  request_menu.delete()
  return redirect('requestapp:requests')

@login_required
def send_request(request):
  group = None
  requests = None
  try:
    group = Group.objects.get(owner=request.user)
    requests = Requests.objects.get(requests_owner=request.user)
    group.requests = requests
    group.save()
  except ObjectDoesNotExist:
    pass
  return redirect('menuapp:list')

@login_required
def cancel_send_request(request):
  group = None
  requests = None
  try:
    group = Group.objects.get(owner=request.user)
    group.requests = None
    group.save()
  except ObjectDoesNotExist:
    pass
  return redirect('menuapp:list')

@login_required
def answer_request(request, request_menu_id):
  group_member = GroupMember.objects.get(member=request.user)
  group_member.request_menu = RequestMenu.objects.get(id=request_menu_id)
  group_member.save()
  return redirect('menuapp:menu')

@login_required
def request_clear(request):
  group = None
  group_member = None
  requests = None
  user = None

  group = Group.objects.get(owner=request.user)
  group_members = GroupMember.objects.filter(group=group)
  requests = Requests.objects.get(requests_owner=request.user)
  request_menus = RequestMenu.objects.filter(requests=requests)
  user = User.objects.get(id=request.user.id)

  user.is_invitated = False
  user.belong_group = False
  user.save()

  group.requests = None
  group.save()

  for group_member in group_members:
    group_member.request_menu = None
    group_member.save()

  for request_menu in request_menus:
    request_menu .delete()

  return redirect('menuapp:menu')