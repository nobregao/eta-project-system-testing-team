import pytest

from pages.CustomerPage import CustomerPage
from pages.LoginPage import LoginPage
from pages.ManagerPage import ManagerPage
from pages.TransactionAccountPage import TransactionAccountPage


@pytest.fixture
def login_page():
    login_page = LoginPage()
    login_page.open()

    yield login_page

    login_page.close()


@pytest.fixture
def customer_page(login_page):
    login_page.make_login_customer()

    customer_page = CustomerPage(login_page.driver)

    yield customer_page

    customer_page.close()


@pytest.fixture
def manager_page(login_page):
    login_page.make_login_manager()

    manager_page = ManagerPage(login_page.driver)

    yield manager_page

    manager_page.close()

@pytest.fixture
def transaction_withdrawl_account(customer_page):
    customer_page.select_exists_account()
    customer_page.click_login_btn()
    transaction_account = TransactionAccountPage(customer_page.driver)
    transaction_account.select_withdrawl_value_account()

    yield transaction_account

    transaction_account.close()

