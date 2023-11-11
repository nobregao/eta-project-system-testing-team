from pages.TransactionAccountPage import TransactionAccountPage


class TestCt7:

    def test_deposit_account(self, customer_page):
        value_deposit = 20.00

        customer_page.is_url(), 'Aplicação não foi para página da cliente'
        customer_page.select_exists_account("Albus Dumbledore")
        customer_page.click_login_btn()

        transaction_account = TransactionAccountPage(customer_page.driver)
        transaction_account.select_deposit_value_account()
        transaction_account.set_amount_transaction(value_deposit)

        saldo_inic = transaction_account.get_balance()

        transaction_account.click_execute_btn()

        saldo_final = transaction_account.get_balance()

        assert saldo_final == float(saldo_inic + value_deposit)
        assert transaction_account.validate_message("Deposit Successful")
