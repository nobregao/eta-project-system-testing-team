from pages.TransactionAccountPage import TransactionAccountPage


class TestCt8:

    def test_withdrawn_account(self, customer_page):
        value_withdrawn = 20.00

        customer_page.is_url(), 'Aplicação não foi para página da cliente'
        customer_page.select_exists_account("Hermoine Granger")
        customer_page.click_login_btn()

        transaction_account = TransactionAccountPage(customer_page.driver)
        transaction_account.select_withdrawl_value_account()
        transaction_account.set_amount_transaction(value_withdrawn)

        saldo_inicial = transaction_account.get_balance()

        transaction_account.click_execute_btn()

        saldo_final = transaction_account.get_balance()

        assert saldo_final == float(saldo_inicial - value_withdrawn)
        assert transaction_account.validate_message("Transaction successful")
