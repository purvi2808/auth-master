from rest_framework import serializers
from django.contrib.auth.models import User
from .models import task

class taskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=task
        fields=('Title','Body')


