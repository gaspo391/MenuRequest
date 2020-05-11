# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import CreateView
# from menuapp.models import Menu
# from requestapp.models import Requests, RequestMenu
# from .models import GroupUser
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class MenuCreate(LoginRequiredMixin, CreateView):
#   template_name = 'account/make_group.html'
#   model = GroupUser
#   fields = ('name')
#   success_url = reverse_lazy('menuapp:menu')
