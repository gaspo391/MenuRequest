from django.db import models
from menuapp.models import Menu
from django.contrib.auth import get_user_model

User = get_user_model()

class Requests(models.Model):
    # requests_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    requests_owner = models.OneToOneField(User, verbose_name='リクエスト発行者', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Requests'
        ordering = ['date_added']

    def __str__(self):
        return self.requests_owner.username

class RequestMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    requests = models.ForeignKey(Requests, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'RequestMenu'

    def __str__(self):
        return self.menu.menuName