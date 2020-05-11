from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Group, GroupMember, GroupInvitatedMember
from menuapp.models import Menu
from requestapp.models import Requests, RequestMenu
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import GroupForm

User = get_user_model()

# class MakeCreate(LoginRequiredMixin, CreateView):
#   template_name = 'group/make_group.html'
#   model = Group
#   fields = ('name', 'requests', 'owner')
#   success_url = reverse_lazy('menuapp:menu')

# def make_group(request):
#     if request.method == 'POST':
#         form = GroupForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             request.user.belong_group = True
#             request.user.save()
#             return redirect(request.META['HTTP_REFERER'])
#     else:
#         form = GroupForm()
#     return render(request, 'group/make_group.html', {'form': form})

def make_group(request):
  form = GroupForm(request.POST)
  
  if form.is_valid():
      form.save()
      request.user.belong_group = True
      request.user.is_invitated = True
      request.user.save()
      return redirect(request.META['HTTP_REFERER'])
  else:
    return redirect(request.META['HTTP_REFERER'])

def delete_group(request):
  group = Group.objects.get(owner=request.user)
  group.delete()
  request.user.belong_group = False
  request.user.is_invitated = False
  request.user.save()
  return redirect(request.META['HTTP_REFERER'])

# def register_member(request):
#   if request.method == 'POST':
#     form = GroupMemberForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('menuapp:menu')
#   else:
#     form = GroupMemberForm()
#   return render(request, 'group/register_member.html', {'form': form})

def invitate_group(request, user_id):
  group = Group.objects.get(owner=request.user)
  user = User.objects.get(id=user_id)
  group_member = None
  try:
    group_member = GroupInvitatedMember.objects.get(
      group = group,
      member = user
    )
  except GroupInvitatedMember.DoesNotExist:
    group_member = GroupInvitatedMember.objects.create(
      group = group,
      member = user
    )
    group_member.save()
    user.is_invitated = True
    user.save()
  return redirect(request.META['HTTP_REFERER'])

def participate_group(request, group_id):
  group = Group.objects.get(id=group_id)
  group_member = None
  invitated_member = GroupInvitatedMember.objects.get(group=group,member=request.user)
  invitated_member.delete()
  try:
    group_member = GroupMember.objects.get(
      group = group,
      member = request.user
    )
  except GroupMember.DoesNotExist:
    group_member = GroupMember.objects.create(
      group = group,
      member = request.user
    )
    group_member.save()
    request.user.belong_group = True
    request.user.save()
  return redirect('menuapp:menu')

def add_member(request, user_id):
  group = Group.objects.get(owner=request.user)
  group_member = None
  try:
    group_member = GroupMember.objects.get(
      group = group,
      member = User.objects.get(id=user_id)
    )
  except GroupMember.DoesNotExist:
    group_member = GroupMember.objects.create(
      group = group,
      member = User.objects.get(id=user_id)
    )
    group_member.member.belong_group = True
    group_member.save()
  return redirect(request.META['HTTP_REFERER'])

def remove_member(request, user_id):
  group = Group.objects.get(owner=request.user)
  group_member = GroupMember.objects.get(
      group = group,
      member = User.objects.get(id=user_id)
    )
  group_member.delete()
  user = User.objects.get(id=user_id)
  user.is_invitated = False
  user.belong_group = False
  user.save()
  return redirect(request.META['HTTP_REFERER'])

def member_list(request):
  group = None
  group_members = None
  group_member = None
  group_owner = None
  try:
    group = Group.objects.get(owner=request.user)
    try:
      group_owner = group.owner
      group_members = GroupMember.objects.filter(group = group)
      try:
        invitated_members = GroupInvitatedMember.objects.filter(group = group)
      except GroupInvitatedMember.DoesNotExist:
        invitated_members = None
    except GroupMember.DoesNotExist:
      group_members = None
  except Group.DoesNotExist:
    try:
      group_member = GroupMember.objects.get(member = request.user)
      group = group_member.group
      group_members = GroupMember.objects.filter(group = group)
      group_owner = group.owner
      invitated_members = None
    except GroupMember.DoesNotExist:
      group = None
      group_members = None
      group_owner = None
      invitated_members = None

  return render(request, 'group/member_list.html', {'group_members':group_members, 'invitated_members':invitated_members, 'group_owner':group_owner})

def invitated_list(request):
  invitated_groups = GroupInvitatedMember.objects.filter(member = request.user)
  return render(request, 'group/invitated_list.html', {'invitated_groups':invitated_groups})