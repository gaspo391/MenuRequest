# Generated by Django 3.0.4 on 2020-04-26 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requestapp', '0001_initial'),
        ('groupapp', '0002_auto_20200426_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='requests',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='requestapp.Requests'),
        ),
    ]
