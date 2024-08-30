from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authapp.api.urls')),

    path('api/', include('taskcollection.urls')),
    path('api/', include('taskcollection.taskstatus.urls')),
    path('api/', include('todo.urls')),
]
