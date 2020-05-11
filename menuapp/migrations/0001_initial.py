# Generated by Django 3.0.4 on 2020-04-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuName', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='media')),
                ('items', models.TextField()),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'menuapp_menu',
            },
        ),
    ]