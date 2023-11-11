import time

from pages.TransactionAccountPage import TransactionAccountPage


class TestCt09:

    def test_transaction_statements_account(self, transaction_withdrawl_account):

        transaction_account = transaction_withdrawl_account
        valor_transaction = transaction_account.set_amount_transaction(20.00)
        transaction_account.click_execute_btn()
        transaction_account.select_trasaction_statements()
        transaction_account.table_trasactions_report()
