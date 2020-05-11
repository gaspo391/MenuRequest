from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UserAdmin(UserAdmin):
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_invitated', 'belong_group', )}),
    )

admin.site.register(User, UserAdmin)