from selenium.webdriver.common.by import By

from pages.Page import Page


class CustomerListPage(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def get_customers_in_table(self):
        td_elements = self.get_elements(By.CSS_SELECTOR, "tbody td:nth-child(1)", 7)
        customers = list(map(lambda td: td.text, td_elements))

        return customers

    def sort_table_for_first_name_alphabetically(self):
        first_column = self.get_element(By.CSS_SELECTOR, "thead tr td:first-child a", 7)
        first_column.click()
        first_column.click()

