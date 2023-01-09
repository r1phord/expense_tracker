from django.test import TestCase
from django.utils import timezone
from transactions.models import Transaction

class TransactionTests(TestCase):
    def create_transaction(self, amount, date=timezone.now(), category=''):
      transaction = Transaction.objects.create(amount=amount, date=date, category=category)
      return transaction

    def test_create_transaction(self):
        transaction = self.create_transaction(123)
        transaction_from_db = Transaction.objects.get(id = transaction.id)
        self.assertIs(transaction, transaction)

    # def test_create_transaction_with_future_date():
    #     ...

    # def test_create_transaction_without_category():
    #     ...

    # def test_create_transaction_with_negative_amount():
    #     ...

    # def test_create_transaction_without_date():
    #     ...
