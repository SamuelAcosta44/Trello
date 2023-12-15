from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def task_api_view(request, pk=None):
    if request.method == 'GET':
        # Operación GET: Obtener lista de tareas o detalles de una tarea específica
        if pk is None:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            task = get_object_or_404(Task, id=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)

    elif request.method == 'POST':
        # Operación POST: Agregar una nueva tarea
        serializer = TaskSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method in ['PUT', 'PATCH']:
        # Operación PUT o PATCH: Actualizar una tarea existente
        task = get_object_or_404(Task, id=pk)
        original_data = TaskSerializer(task).data

        serializer = TaskSerializer(instance=task, data=request.data, partial=request.method == 'PATCH')

        if serializer.is_valid():
            serializer.save()
            response_data = {'original_data': original_data, 'updated_data': serializer.data}
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)