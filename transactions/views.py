from django.shortcuts import render

def index_view(request):
    return render(request, 'transactions/index.html')

def transactions_view(request):
    return render(request, 'transactions/transactions.html')

def reminders_view(request):
    return render(request, 'transactions/reminders.html')

def reports_view(request):
    return render(request, 'transactions/reports.html')

def budget_view(request):
    return render(request, 'transactions/budget.html')

def accounts_view(request):
    return render(request, 'transactions/accounts.html')

def categories_view(request):
    return render(request, 'transactions/categories.html')

def settings_view(request):
    return render(request, 'transactions/settings.html')