# Generated by Django 4.0.3 on 2022-05-25 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_lastlogin_user_lastlogout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lastlogin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastlogout',
        ),
    ]
