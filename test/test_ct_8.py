import time

from pages.TransactionAccountPage import TransactionAccountPage


class TestCt08:

    def test_Withdrawn_account(self, customer_page):
        value_withdrawn = 20.00

        customer_page.is_url(), 'Aplicação não foi para página da cliente'
        customer_page.select_exists_account()
        customer_page.click_login_btn()
        transaction_account = TransactionAccountPage(customer_page.driver)
        transaction_account.select_withdrawl_value_account()
        transaction_account.set_amount_transaction(value_withdrawn)
        saldo_inic = transaction_account.getBalance()
        transaction_account.click_execute_btn()
        saldo_final = transaction_account.getBalance()
        assert saldo_final == float(saldo_inic - value_withdrawn)
        assert transaction_account.validateMessage("Transaction successful")
