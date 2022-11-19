from django.urls import path
from .views import (
    home,
    get_tasks_view,
)

urlpatterns = [
    path('', home),
    path('tasks/', get_tasks_view),
]
