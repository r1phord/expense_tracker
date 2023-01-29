from django.urls import path

from . import views

urlpatterns = [
    path('browse/', views.index_view, name='browse'),
    path('transactions/', views.transactions_view, name='transactions'),
    path('reminders/', views.reminders_view, name='reminders'),
    path('reports/', views.reports_view, name='reports'),
    path('budget/', views.budget_view, name='budget'),
    path('accounts/', views.accounts_view, name='accounts'),
    path('categories/', views.categories_view, name='categories'),
    path('settings/', views.settings_view, name='settings'),
]