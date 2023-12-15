from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data = request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET', 'PUT'])
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
            serializer = TaskSerializer(task)
            return Response(serializer.data)
    elif request.method == 'PUT':
        original_data = TaskSerializer(task).data
        serializer = TaskSerializer(instance=task, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            response_data = {'updated_data': serializer.data}
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
