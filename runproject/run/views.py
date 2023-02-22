from .models import Run
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RunSerializer

# Create your views here.
class RunViewSet(viewsets.ModelViewSet):
    #load into frontend -> filter results per route params -> crunch the numbers -> display analytics
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    permission_classes = [permissions.AllowAny]

