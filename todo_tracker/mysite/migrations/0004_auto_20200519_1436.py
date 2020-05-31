# Generated by Django 3.0.6 on 2020-05-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_task_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='canceled',
            field=models.BooleanField(default=False, verbose_name='Mark task canceled?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='completion',
            field=models.BooleanField(default=False, verbose_name='Mark task completed?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Make task private?'),
        ),
    ]