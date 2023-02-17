from .models import Spice
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SpiceSerializer

# Create your views here.
class SpiceViewSet(viewsets.ModelViewSet):
    #Index route
    queryset = Spice.objects.all()
    #For serializing all objects
    serializer_class = SpiceSerializer
    #Optional permission class to set permission level
    permission_classes = [permissions.AllowAny]