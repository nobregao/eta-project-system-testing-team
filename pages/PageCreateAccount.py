from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Page import Page


class PageCreateAccount(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount"

    element_select_list_names_customer = 'userSelect'
    element_option_name = '#userSelect > option'
    element_select_list_currency = 'currency'
    element_option_currency = '#currency > option'
    element_process_btn = 'button[type="submit"]'

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def select_customer_name(self, customer_name):
        select_customer = self.get_element(By.ID, self.element_select_list_names_customer)
        Select(select_customer).select_by_visible_text(customer_name)

    def select_currency(self, currency_name):
        select_currency = self.get_element(By.ID, self.element_select_list_currency)
        Select(select_currency).select_by_visible_text(currency_name)

    def click_process_btn(self):
        self.get_element(By.CSS_SELECTOR, self.element_process_btn).click()
