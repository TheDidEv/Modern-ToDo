from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from taskcollection.taskstatus.serializers import TaskStatusSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_status(request, coll_id):
    request_data = request.data

    merge_data = request_data
    merge_data['collection'] = coll_id

    serializer = TaskStatusSerializer(data=merge_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)