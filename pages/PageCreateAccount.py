from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Page import Page

class   PageCreateAccount(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount"
    element_select_list_names_customer = 'userSelect'
    element_option_name = '#userSelect > option'
    element_select_list_currency = 'currency'
    element_option_currency = '#currency > option'
    element_process_btn = 'button[type="submit"]'

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def select_customer_name(self):
        select_customer = self.get_element(By.ID, self.element_select_list_names_customer)
        customer_list = self.driver.find_elements(By.CSS_SELECTOR, self.element_option_name)
        random_index = randint(0, len(customer_list) - 1)
        Select(select_customer).select_by_visible_text('Harry Potter')

    def select_currency(self):
        select_currency = self.get_element(By.ID, self.element_select_list_currency)
        currency_list = self.driver.find_elements(By.CSS_SELECTOR, self.element_option_currency)
        random_index = randint(0, len(currency_list) - 1)
        Select(select_currency).select_by_visible_text('Dollar')

    def click_process_btn(self):
        self.get_element(By.CSS_SELECTOR, self.element_process_btn).click()

