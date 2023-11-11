import pytest

from pages.PageAddCustomer import PageAddCustomer
from selenium.webdriver.common.alert import Alert

class TestCt1:

        def test_add_customer(self, manager_page):
                manager_page.click_aba_add_customer()
                pageAddCustomer = PageAddCustomer(driver=manager_page.driver)
                pageAddCustomer.insert_customer_data()
                pageAddCustomer.click_add_customer_btn()
                alert = Alert(pageAddCustomer.driver)
                assert alert.text.startswith('Customer added successfully')






