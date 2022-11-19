from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import Task

from .serializers import TaskSerializer


@api_view(['GET'])
def home(request: Request) -> Response:
    '''home'''
    return Response({'endpoints': 'home'})


@api_view(['GET'])
def get_tasks_view(request: Request) -> Response:
    '''home'''
    tasks = Task.objects.all()
    tasks_list = TaskSerializer(tasks, many=True).data
    
    return Response({'tasks':tasks_list})
