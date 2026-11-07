from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentModifyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer