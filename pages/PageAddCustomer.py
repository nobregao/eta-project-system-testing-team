from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from pages.Page import Page

class   PageAddCustomer(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def insert_customer_data(self, first_name='Equipe', last_name='5', post_code='12345'):
        self.get_element(By.CSS_SELECTOR, '[ng-model="fName"]').send_keys(first_name)
        self.get_element(By.CSS_SELECTOR, '[ng-model="lName"]').send_keys(last_name)
        self.get_element(By.CSS_SELECTOR, '[ng-model="postCd"]').send_keys(post_code)

    def click_add_customer_btn(self):
        self.get_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        alert = Alert(self.driver)
        text_alert = alert.text

        alert.accept()

        return text_alert
