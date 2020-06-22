from django.urls import path
from . import views
from .views import (
    TransactionDetailView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDeleteView,
    )

urlpatterns = [
    path('', views.home_view, name='MainScreen-home'),
    path('statisctics', views.statistics_view, name='statistics'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('transaction/new/', TransactionCreateView.as_view(), name='transaction-create'),
]