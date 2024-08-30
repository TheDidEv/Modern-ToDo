from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import TaskCollection
from .serializers import TaskCollectionSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_collections(request):
    user = request.user
    
    task_collections = TaskCollection.objects.filter(user=user)
    
    if not task_collections.exists():
        return Response(
            {"message": "You hane no task collections"},
            status=status.HTTP_200_OK,
        )
    
    serialize = TaskCollectionSerializer(task_collections, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_task(request):
    user = request.user

    merge_data = request.data
    merge_data['user'] = user.id

    serializer = TaskCollectionSerializer(data=merge_data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
# pk - uri params
def put_task(request, pk):
    user = request.user

    # get found object by pk and user
    try:
        task_collection = TaskCollection.objects.get(pk=pk, user=user)
    except TaskCollection.DoesNotExist:
        return (Response(
            {"message:": "Task collection not found"}),
            status.HTTP_404_NOT_FOUND
        )

    merge_data = request.data
    merge_data['user'] = user.id

    # update object if data valid
    serializer = TaskCollectionSerializer(task_collection, data=merge_data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    user = request.user

    try:
        task_collection = TaskCollection.objects.get(pk=pk, user=user)
    except TaskCollection.DoesNotExist:
        return Response({"message:": "Task collection not found"}), status.HTTP_404_NOT_FOUND

    task_collection.delete()
    return Response({"message:": "Task collection deleted"}, status=status.HTTP_200_OK)
