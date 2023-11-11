from selenium.webdriver.common.by import By

from pages.Page import Page


class ManagerPage(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def click_aba_add_customer(self):
        button = self.get_element(By.CSS_SELECTOR, "[ng-class='btnClass1']", 10)
        button.click()

    def click_aba_open_account(self):
        button = self.get_element(By.CSS_SELECTOR, "[ng-class='btnClass2']")
        button.click()

    def click_aba_customers(self):
        button = self.get_element(By.CSS_SELECTOR, "[ng-class='btnClass3']", 10)
        button.click()

