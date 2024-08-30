from django.urls import path

from taskcollection.taskstatus.views import add_status

urlpatterns = [
    path('add-status/<int:coll_id>', add_status, name='add-status')
]