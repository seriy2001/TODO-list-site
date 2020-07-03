from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startdate = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField(default=None, blank=True, null=True, 
      verbose_name="Duedate (YYYY-MM-DD HH:MM)")
    completion = models.BooleanField(default=False,
                                     verbose_name="Mark task completed?")
    canceled = models.BooleanField(default=False,
                                   verbose_name="Mark task canceled?")
    public = models.BooleanField(default=False,
                                 verbose_name="Make task public? "
                                              "(Your task will be publicly "
                                              "available for everyone to "
                                              "view, but not edit)")
    note = models.TextField(default=None, max_length=1000,
                            blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/'
