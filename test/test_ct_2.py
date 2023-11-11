import pytest

from pages.PageAddCustomer import PageAddCustomer
from selenium.webdriver.common.alert import Alert

from pages.PageCreateAccount import PageCreateAccount


class TestCt2:

    def test_open_account_sucess(self, manager_page):
        manager_page.click_aba_open_account()
        pageCreateAccount = PageCreateAccount(driver=manager_page.driver)
        pageCreateAccount.select_customer_name()
        pageCreateAccount.select_currency()
        pageCreateAccount.click_process_btn()
        alert = Alert(pageCreateAccount.driver)
        assert alert.text.startswith('Account created successfully')

