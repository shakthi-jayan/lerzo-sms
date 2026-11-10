from rest_framework import generics
from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentListAPI(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentModifyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer