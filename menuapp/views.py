from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Menu
from requestapp.models import Requests, RequestMenu
from groupapp.models import Group, GroupMember
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@login_required
def menufunc(request):
  group = None
  group_member = None
  try:
    group = Group.objects.get(owner=request.user)
    group_member = GroupMember.objects.filter(group=group)
  except ObjectDoesNotExist:
    pass
  return render(request, 'menu/menu.html', {'group_member':group_member})

def _requests_id(request):
    requests = request.session.session_key
    if not requests:
        requests = request.session.create()
    return requests

@login_required
def menu_list(request):
  username = request.user.get_username()
  menu = Menu.objects.filter(author=username)
  requests = None
  request_menus = []
  # requests = Requests.objects.get(requests_id=_requests_id(request))
  # request_menus = list(RequestMenu.objects.filter(requests=requests).values_list('menu', flat=True))

  try:
    # requests = Requests.objects.get(requests_id=_requests_id(request))
    requests = Requests.objects.get(requests_owner=request.user)
    request_menus = list(RequestMenu.objects.filter(requests=requests).values_list('menu', flat=True))
  except ObjectDoesNotExist:
    pass

  return render(request, 'menu/list.html', {'object_list':menu, 'request_menus':request_menus})

class MenuDetail(LoginRequiredMixin, DetailView):
  template_name = 'menu/detail.html'
  model = Menu

class MenuCreate(LoginRequiredMixin, CreateView):
  template_name = 'menu/create.html'
  model = Menu
  fields = ('menuName', 'category', 'image', 'items', 'author')
  success_url = reverse_lazy('menuapp:list')

class MenuDelete(LoginRequiredMixin, DeleteView):
  # template_name = 'menu/delete.html'
  model = Menu
  success_url = reverse_lazy('menuapp:list')

class MenuRequest(LoginRequiredMixin, ListView):
  template_name = 'menu/menurequest.html'
  model = Menu
  def get_queryset(self):
    username = self.request.user.get_username()
    queryset = Menu.objects.filter(author=username)
    return queryset
  