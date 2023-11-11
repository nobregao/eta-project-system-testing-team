from selenium.webdriver.common.by import By

from pages.Page import Page
from selenium.webdriver.support.select import Select


class CustomerPage(Page):
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
    element_select_name = 'userSelect'
    element_option_name = '#userSelect > option'
    element_btn = 'button[type="submit"]'

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def select_exists_account(self, customer_name):
        select_element = self.get_element(By.ID, self.element_select_name)
        Select(select_element).select_by_visible_text(customer_name)

    def click_login_btn(self):
        button = self.get_element(By.CSS_SELECTOR, self.element_btn)
        button.click()
