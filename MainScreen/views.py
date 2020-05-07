from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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
    ordering = ['-date']

class TransactionDetailView(DetailView):
    model = Transaction

class TransactionCreateView(CreateView):
    model = Transaction
    fields = ['value', 'destination']

    def form_valid(self, form):
        form.instance.transaction_user = self.request.user
        return super().form_valid(form)


