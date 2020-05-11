from django import forms
from .models import Group, GroupMember

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'requests', 'owner')