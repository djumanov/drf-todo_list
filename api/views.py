from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def home(request: Request) -> Response:
    '''home'''
    return Response({'endpoints': 'home'})
