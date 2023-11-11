import pytest

from pages.CustomerPage import CustomerPage
from pages.LoginPage import LoginPage
from pages.ManagerPage import ManagerPage


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
