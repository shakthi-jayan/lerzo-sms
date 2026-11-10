from rest_framework import generics
from django.db.models import Sum, DecimalField, F, Value
from django.db.models.functions import Coalesce
from .models import Payment
from enrollments.models import Enrollment
from .serializers import PaymentSerializer, EnrollmentFeeSummarySerializer

class PaymentListAPI(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentModifyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class FeeSummaryListAPI(generics.ListAPIView):
    serializer_class = EnrollmentFeeSummarySerializer

    def get_queryset(self):
        return Enrollment.objects.annotate(
            annotated_total_paid=Coalesce(
                Sum('payments__amount_paid'), 
                Value(0.00), 
                output_field=DecimalField()
            ),
            annotated_course_fee=F('batch__course__fee_amount'),
            annotated_pending_balance=F('batch__course__fee_amount') - Coalesce(
                Sum('payments__amount_paid'), 
                Value(0.00), 
                output_field=DecimalField()
            )
        )