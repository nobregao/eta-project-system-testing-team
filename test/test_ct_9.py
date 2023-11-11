class TestCt9:

    def test_transaction_account_different(self, transaction_deposit_account):

        transaction_account = transaction_deposit_account

        value_deposit_account = 20.00

        balance_account1_inicial = transaction_account.get_balance()

        transaction_account.select_account("1014")
        balance_account2_inicial = transaction_account.get_balance()
        transaction_account.set_amount_transaction(value_deposit_account)
        transaction_account.click_execute_btn()
        balance_account2_final = transaction_account.get_balance()
        assert balance_account2_final == (balance_account2_inicial + value_deposit_account)

        transaction_account.select_account("1013")

        balance_account1_final = transaction_account.get_balance()

        assert balance_account1_inicial == balance_account1_final
