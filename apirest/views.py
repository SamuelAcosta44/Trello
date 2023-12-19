from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SimpleAuthenticationForm
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = SimpleAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(task_api_view)
    else:
        form = SimpleAuthenticationForm()

    return render(request, 'login.html', {'form': form})

@api_view(['GET'])
def filter_by_status(request, status):
    queryset = Task.objects.filter(status=status) if status else Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filter_by_deadline(request, deadline):
    queryset = Task.objects.filter(deadline=deadline) if deadline else Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filter_by_name(request, name):
    queryset = Task.objects.filter(name__icontains=name) if name else Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def task_api_view(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            task = get_object_or_404(Task, id=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)

    elif request.method == 'POST':
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
        task = get_object_or_404(Task, id=pk)
        original_data = TaskSerializer(task).data

        serializer = TaskSerializer(instance=task, data=request.data, partial=request.method == 'PATCH')

        if serializer.is_valid():
            serializer.save()
            response_data = {'original_data': original_data, 'updated_data': serializer.data}
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)