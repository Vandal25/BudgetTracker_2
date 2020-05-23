from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Transaction

def home(request):
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'MainScreen/Home.html', context)

class TransactionListView(ListView):
    model = Transaction
    template_name = 'MainScreen/Home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'transactions'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user.id
        return Transaction.objects.filter(transaction_user=user).order_by('-date')

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



