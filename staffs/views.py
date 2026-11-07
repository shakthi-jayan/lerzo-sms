from rest_framework import generics
from .models import Staff
from .serializers import StaffSerializer

class StaffListAPI(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffModifyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer