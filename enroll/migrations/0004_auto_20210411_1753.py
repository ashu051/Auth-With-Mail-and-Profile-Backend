# Generated by Django 3.1.7 on 2021-04-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_friend_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend_request',
            name='friends',
            field=models.ManyToManyField(blank=True, max_length=40, null=True, to='enroll.User'),
        ),
    ]
