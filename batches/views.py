from rest_framework import generics
from .models import Batch
from .serializers import BatchSerializer

class BatchListAPI(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BatchModifyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer