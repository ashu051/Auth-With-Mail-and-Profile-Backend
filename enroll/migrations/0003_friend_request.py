# Generated by Django 3.1.7 on 2021-04-11 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210409_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(blank=True, max_length=40, to='enroll.User')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='enroll.user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='enroll.user')),
            ],
        ),
    ]
