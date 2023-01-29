from django.shortcuts import render

def index_view(request):
    return render(request, 'transactions/index.html')

def all_transactions_view(request):
    ...

def update_transaction_view(request, transaction_id):
    ...

def delete_transaction_view(request, transaction_id):
    ...
