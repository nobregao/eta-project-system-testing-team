from selenium.webdriver.common.by import By

from pages.Page import Page


class CustomerListPage(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"

    css_selector_table_customer = "tbody td:nth-child(1)"
    css_selector_first_td_thead_table_customer = "thead tr td:first-child a"
    css_selector_input = "input"

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def get_customers_in_table(self):
        td_elements = self.get_elements(By.CSS_SELECTOR, self.css_selector_table_customer, 7)
        customers = list(map(lambda td: td.text, td_elements))

        return customers

    def sort_table_for_first_name_alphabetically(self):
        first_column = self.get_element(By.CSS_SELECTOR, self.css_selector_first_td_thead_table_customer, 7)
        first_column.click()
        first_column.click()

    def search_customer(self, customer_name):
        input_element = self.get_element(By.CSS_SELECTOR, self.css_selector_input)
        input_element.send_keys(customer_name)
