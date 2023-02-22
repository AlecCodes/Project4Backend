from .models import Run
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    model = Run
    fields = ['name','dur','distance', 'category']