# Generated by Django 3.0.6 on 2020-05-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='completion',
            field=models.BooleanField(default=False),
        ),
    ]
