# Generated by Django 3.2.14 on 2022-08-07 08:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220725_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='folloing',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_users_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
