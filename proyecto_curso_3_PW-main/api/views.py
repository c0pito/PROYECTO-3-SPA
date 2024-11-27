from .models import boleteria 
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import boleteriaSerializer

# Create your views here.
class boleteriaViewSet(viewsets.ModelViewSet):
    queryset=boleteria.objects.all().order_by('-fecha_concierto')
    serializer_class= boleteriaSerializer
    