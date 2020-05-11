from django.db import models
from django.contrib.auth import get_user_model
from requestapp.models import Requests, RequestMenu

User = get_user_model()

# Create your models here.
class Group(models.Model):
  title = models.CharField(verbose_name='グループ名', max_length=250)
  requests = models.ForeignKey(Requests, on_delete=models.CASCADE, blank=True, null=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'Group'
  
  def __str__(self):
    return str(self.title)

class GroupMember(models.Model):
  member = models.ForeignKey(User, on_delete=models.CASCADE)
  group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
  request_menu = models.ForeignKey(RequestMenu, on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
    db_table = 'GroupMember'
  
  def __str__(self):
    return str(self.member.username)

class GroupInvitatedMember(models.Model):
  member = models.ForeignKey(User, on_delete=models.CASCADE)
  group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
    db_table = 'GroupInvitatedMember'
  
  def __str__(self):
    return str(self.member.username)