from django.urls import path
from . import views
from .views import PublicListView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView, PrivateListView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('', PublicListView.as_view(), name='tracker_home'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(
        template_name='mysite/edit_task.html'), name='edit_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(),
         name='delete_task'),
    path('private/', PrivateListView.as_view(), name='private_tasks')
]
