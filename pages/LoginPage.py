from selenium.webdriver.common.by import By

from pages.Page import Page


class LoginPage(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    def __init__(self):
        super().__init__(self.url)

    def make_login_customer(self):
        button = self.get_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg[ng-click='customer()']", 10)
        button.click()

    def make_login_manager(self):
        button = self.get_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg[ng-click='manager()']", 10)
        button.click()
