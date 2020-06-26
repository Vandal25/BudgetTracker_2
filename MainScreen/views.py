from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Transaction
from django.db.models import Sum
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def home(request):
    context = {
        'transactions': Transaction.objects.all(),
        'total': Transaction.objects.all()
    }
    return render(request, 'MainScreen/Home.html', context)

class TransactionDetailView(DetailView):
    model = Transaction

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['transaction_direction', 'value', 'transaction_type', 'destination']

    def form_valid(self, form):
        form.instance.transaction_user = self.request.user
        return super().form_valid(form)

class TransactionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transaction
    fields = ['transaction_direction', 'value', 'transaction_type', 'destination']

    def form_valid(self, form):
        form.instance.transaction_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Transaction = self.get_object()
        if self.request.user == Transaction.transaction_user:
            return True
        return False

class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    success_url = '/'

    def test_func(self):
        Transaction = self.get_object()
        if self.request.user == Transaction.transaction_user:
            return True
        return False

def home_view(request):
    user = request.user.id
    logging.debug('User {}'.format(user))
    transactions = Transaction.objects.filter(transaction_user=user).order_by('-date')
    total_expenses = Transaction.objects.filter(transaction_user=user, transaction_direction=1).aggregate(Sum('value'))['value__sum']
    total_revenue = Transaction.objects.filter(transaction_user=user, transaction_direction=2).aggregate(Sum('value'))['value__sum']

    def is_not_none(value):
        if value is None:
            value = 0
        logging.debug('Value check: {} '.format(value))
        return value

    total_expenses = is_not_none(total_expenses)
    total_revenue = is_not_none(total_revenue)

    total = total_revenue - total_expenses

    context = {'transactions': transactions,
               'total_expenses': total_expenses,
               'total_revenue': total_revenue,
               'total': total,
               }
    return render(request, 'MainScreen/Home.html', context)

def statistics_view(request):
    user = request.user.id
    logging.debug('User {}'.format(user))
    default = Transaction.objects.filter(transaction_user=user, transaction_type=1, transaction_direction=1).aggregate(Sum('value'))['value__sum']
    entertainment = Transaction.objects.filter(transaction_user=user, transaction_type=2, transaction_direction=1).aggregate(Sum('value'))['value__sum']
    utilities = Transaction.objects.filter(transaction_user=user, transaction_type=3, transaction_direction=1).aggregate(Sum('value'))['value__sum']
    food = Transaction.objects.filter(transaction_user=user, transaction_type=4, transaction_direction=1).aggregate(Sum('value'))['value__sum']
    transport = Transaction.objects.filter(transaction_user=user, transaction_type=5, transaction_direction=1).aggregate(Sum('value'))['value__sum']

    def is_not_none(value):
        if value is None:
            value = 0
        logging.debug('Value check: {} '.format(value))
        return value

    default = is_not_none(default)
    entertainment = is_not_none(entertainment)
    utilities = is_not_none(utilities)
    food = is_not_none(food)
    transport = is_not_none(transport)

    context = {'default': default,
               'entertainment': entertainment,
               'utilities': utilities,
               'food': food,
               'transport': transport,
    }
    return render(request, 'MainScreen/statistics.html', context)


