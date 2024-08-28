from django.urls import path
from .views import get_all_collections, put_task, post_task, delete_task

urlpatterns = [
    path('task-collections/', get_all_collections, name='task-collections'),
    path('create-collection/', post_task, name='create-collection'),
    path('update-collection/<int:pk>', put_task, name='update-collection'),
    path('delete-collection/<int:pk>', delete_task, name='delete-collection'),
]