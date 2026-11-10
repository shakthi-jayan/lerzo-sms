from rest_framework import serializers
from .models import Payment
from enrollments.models import Enrollment

class PaymentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='enrollment.student.first_name', read_only=True)
    course_name = serializers.CharField(source='enrollment.batch.course.title', read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id', 
            'enrollment', 
            'student_name', 
            'course_name', 
            'amount_paid', 
            'payment_date', 
            'transaction_id', 
            'receipt_number', 
            'payment_method', 
            'remarks'
        ]

    def validate(self, attrs):
        enrollment = attrs.get('enrollment')
        amount_paid = attrs.get('amount_paid')

        if amount_paid <= 0:
            raise serializers.ValidationError({"amount_paid": "Payment amount must be greater than zero."})

        # Check overpayment validation against pending balance
        if enrollment and amount_paid > enrollment.pending_balance:
            raise serializers.ValidationError({
                "amount_paid": f"Amount exceeds pending balance of {enrollment.pending_balance}"
            })

        return attrs


class EnrollmentFeeSummarySerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.first_name', read_only=True)
    course_title = serializers.CharField(source='batch.course.title', read_only=True)
    course_fee = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    total_paid = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    pending_balance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            'id', 
            'student', 
            'student_name', 
            'batch', 
            'course_title', 
            'course_fee', 
            'total_paid', 
            'pending_balance', 
            'payments'
        ]