# Generated by Django 3.0.4 on 2020-04-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='belong_group',
            field=models.BooleanField(default=False, help_text='グループに所属しているかどうか ', verbose_name='belong group'),
        ),
    ]