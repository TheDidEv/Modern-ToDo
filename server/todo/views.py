from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from taskcollection.taskstatus.models import TaskStatus
from .models import ToDo
from .serializers import ToDoSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request, coll_id):
    tasks = ToDo.objects.filter(collection=coll_id)

    if not tasks.exists():
        return Response(
            {"message": "No tasks found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serialize = ToDoSerializer(tasks, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task(request, coll_id):
    request = request.data

    try:
        TaskStatus.objects.get(collection=coll_id, name=request['status'])
    except TaskStatus.DoesNotExist:
        return Response(
            {"message": "No task status found. Please create status, before create task"},
            status=status.HTTP_404_NOT_FOUND
        )

    merge_data = request
    merge_data['collection'] = coll_id

    serializer = ToDoSerializer(data=merge_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, todo_id):
    task = get_object_or_404(ToDo, id=todo_id)
    request = request.data

    try:
        TaskStatus(collection=task.collection, name=request['status'])
    except TaskStatus.DoesNotExist:
        return Response(
            {"message": "No task status found. Please create status, before update task"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ToDoSerializer(task, data=request)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_task(request, coll_id):
