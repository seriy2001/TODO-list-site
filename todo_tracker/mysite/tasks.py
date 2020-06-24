# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail


@shared_task
def task_duedate_notification_mail():
	send_mail('TODO tracker: your task\'s due date is coming up!',
		'Hello, please check the task and mark it \"completed\" or \"canceled\"',
		'todo.tracker.dev@gmail.com',
		['vehepil594@wkernl.com'])
	return None