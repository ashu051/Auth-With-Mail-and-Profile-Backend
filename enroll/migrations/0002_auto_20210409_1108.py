# Generated by Django 3.1.7 on 2021-04-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='message',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
