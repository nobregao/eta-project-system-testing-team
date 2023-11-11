import time

from selenium.webdriver.common.by import By

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
    table_bank_statement = 'tbody>tr'

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def select_trasaction_statements(self):
        transaction_statement = self.get_element(By.CSS_SELECTOR, self.transaction_statements_btn,20)
        transaction_statement.click()

    def select_deposit_value_account(self):
        deposit_transaction = self.get_element(By.CSS_SELECTOR, self.deposit_transaction_btn)
        deposit_transaction.click()

    def select_withdrawl_value_account(self):
        deposit_transaction = self.get_element(By.CSS_SELECTOR, self.withdrawl_transaction_btn)
        deposit_transaction.click()

    def table_trasactions_report(self):
        table = self.get_elements(By.CSS_SELECTOR,self.table_bank_statement,)
        statements = list(map(lambda tr: self.convert_tr_to_td(tr), table))
        return statements

    def convert_tr_to_td(self, tr):
        print(tr)



    def set_amount_transaction(self, value):
        deposit_value = self.get_element(By.CSS_SELECTOR, self.deposit_value_input)
        deposit_value.send_keys(value)

    def click_execute_btn(self):
        button = self.get_element(By.CSS_SELECTOR, self.deposit_btn)
        button.click()

    def getBalance(self):
        value = self.get_elements(By.CSS_SELECTOR, self.balance_value_txt)[1].text
        return float(value)

    def validateMessage(self, message):
        message_text = self.get_element(By.CSS_SELECTOR, self.deposit_message_success)
        return message_text.text == message
