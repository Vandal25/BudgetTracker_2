from django.urls import path
from . import views
from .views import (
    TransactionListView,
    TransactionDetailView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDeleteView,
    )

urlpatterns = [
    path('', TransactionListView.as_view(), name='MainScreen-home'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('transaction/new/', TransactionCreateView.as_view(), name='transaction-create'),
]