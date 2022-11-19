from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Task(models.Model):
    title = models.CharField(max_length=65, blank=False)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duedate = models.DateTimeField(null=True, blank=True)
    importance = models.SmallIntegerField(
        blank=True,
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
