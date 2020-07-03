from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _090
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Task
from .tasks import task_duedate_notification_mail, task_created_notification_mail
from django.urls import reverse


class PublicListView(ListView):
    model = Task
    template_name = 'mysite/home.html'
    context_object_name = 'tasks'
    ordering = ['-startdate']
    # paginate_by = 5


class PrivateListView(LoginRequiredMixin, PublicListView):
    template_name = "mysite/private_tasks.html"
    # paginate_by = 5


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['title', 'duedate', 'note', 'public']
    success_message = f"Task \"%(title)s\" created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        task_created_notification_mail(self.object.id)
        task_duedate_notification_mail.apply_async(args=[self.object.id], eta=self.object.duedate)
        return reverse('tracker_home')


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['title', 'duedate', 'note', 'completion', 'canceled']
    success_message = "Task \"%(title)s\" saved"

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        else:
            return False

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    success_url = '/'
    success_message = "Task \"%(title)s\" deleted"

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        else:
            return False
