from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Page import Page


class TransactionAccountPage(Page):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    deposit_message_success = '[ng-show="message"]'
    balance_value_txt = '[class="ng-binding"]'
    transaction_statements_btn = '[ng-class="btnClass1"]'
    deposit_transaction_btn = '[ng-class="btnClass2"]'
    withdrawl_transaction_btn = '[ng-class="btnClass3"]'
    deposit_btn = 'button[type="submit"]'
    deposit_value_input = '[ng-model="amount"]'
    table_bank_statement = 'tbody td'
    element_select = 'accountSelect'

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def select_deposit_value_account(self):
        deposit_transaction = self.get_element(By.CSS_SELECTOR, self.deposit_transaction_btn)
        deposit_transaction.click()

    def select_withdrawl_value_account(self):
        deposit_transaction = self.get_element(By.CSS_SELECTOR, self.withdrawl_transaction_btn, 3)
        deposit_transaction.click()

    def set_amount_transaction(self, value):
        deposit_value = self.get_element(By.CSS_SELECTOR, self.deposit_value_input, 2)
        deposit_value.send_keys(value)

    def click_execute_btn(self):
        button = self.get_element(By.CSS_SELECTOR, self.deposit_btn, 5)
        button.click()

    def get_balance(self):
        value = self.get_elements(By.CSS_SELECTOR, self.balance_value_txt)[1].text
        return float(value)

    def select_account(self, account_number):
        accounts = self.get_element(By.ID, self.element_select)
        Select(accounts).select_by_visible_text(account_number)

    def validate_message(self, message):
        message_text = self.get_element(By.CSS_SELECTOR, self.deposit_message_success)
        return message_text.text == message
