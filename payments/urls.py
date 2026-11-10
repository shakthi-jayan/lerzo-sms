from django.urls import path
from .views import PaymentListAPI, PaymentModifyAPI, FeeSummaryListAPI

urlpatterns = [
    path('', PaymentListAPI.as_view(), name='payment_list_add'),
    path('<int:pk>/', PaymentModifyAPI.as_view(), name='payment_modify'),
    path('summary/', FeeSummaryListAPI.as_view(), name='fee_summary_list'),
]