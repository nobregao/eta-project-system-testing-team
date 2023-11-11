import time
from random import randint

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

    def select_exists_account(self):
        select_element = self.get_element(By.ID, self.element_select_name)
        account_list = self.driver.find_elements(By.CSS_SELECTOR,self.element_option_name)
        random_index = randint(0, len(account_list) - 1)
        Select(select_element).select_by_visible_text('Hermoine Granger')

    def click_login_btn(self):
      button = self.get_element(By.CSS_SELECTOR, self.element_btn)
      button.click()
