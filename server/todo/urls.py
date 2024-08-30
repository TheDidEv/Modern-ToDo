from django.urls import path
from .views import get_tasks, add_task, update_task

urlpatterns = [
    path('get-tasks/<int:coll_id>', get_tasks, name='get_tasks'),
    path('add-tasks/<int:coll_id>', add_task, name='add_task'),
    path('update-tasks/<int:todo_id>', update_task, name='update_task'),
]