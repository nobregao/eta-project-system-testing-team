from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from pages.Page import Page

class   PageAddCustomer(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"

    css_selector_first_name = '[ng-model="fName"]'
    css_selector_last_name = '[ng-model="lName"]'
    css_selector_post_cod = '[ng-model="postCd"]'
    css_selector_add_customer_btn = 'button[type="submit"]'
    def __init__(self, driver):
        super().__init__(self.url, driver)

    def insert_customer_data(self, first_name='Equipe', last_name='5', post_code='12345'):
        self.get_element(By.CSS_SELECTOR, self.css_selector_first_name).send_keys(first_name)
        self.get_element(By.CSS_SELECTOR, self.css_selector_last_name).send_keys(last_name)
        self.get_element(By.CSS_SELECTOR, self.css_selector_post_cod).send_keys(post_code)

    def click_add_customer_btn(self):
        self.get_element(By.CSS_SELECTOR, self.css_selector_add_customer_btn).click()
        alert = Alert(self.driver)
        text_alert = alert.text
        alert.accept()
        return text_alert
