# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()

@shared_task
def task_duedate_notification_mail(task_pk):
	t = Task.objects.get(pk=task_pk)
	send_mail(f'TODO tracker: your task "{t.title}" due date is coming up!',
		'Hello, please check the task and mark it \"completed\" or \"canceled\"',
		'todo.tracker.dev@gmail.com',
		[t.user.email])
	return None

@shared_task
def task_created_notification_mail(task_pk):
	t = Task.objects.get(pk=task_pk)
	send_mail(f'TODO tracker: you have just created a task "{t.title}"!',
		f'Hello, this is Sergey\'s todo tracker team notifying of \
		successful creation of your task "{t.title}"! Please make sure to mark the task \
		\"completed\" or \"canceled\" as you finish doing it.',
		'todo.tracker.dev@gmail.com',
		[t.user.email])
	return None