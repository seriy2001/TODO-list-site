# Generated by Django 3.0.6 on 2020-05-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20200515_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
