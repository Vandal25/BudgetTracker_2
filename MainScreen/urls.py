from django.urls import path
from . import views
from .views import TransactionListView, TransactionDetailView, TransactionCreateView

urlpatterns = [
    path('', TransactionListView.as_view(), name='MainScreen-home'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction/new/', TransactionCreateView.as_view(), name='transaction-create'),
]