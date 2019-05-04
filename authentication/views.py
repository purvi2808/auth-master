
from rest_framework import viewsets

from . import models
from . import serializers


class taskView(viewsets.ModelViewSet):
    queryset=models.task.objects.all()
    serializer_class=serializers.taskSerializer
