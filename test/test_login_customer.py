from pages.CustomerPage import CustomerPage


class TestLoginCustomer:

    def test_make_login_customer(self, login_page):

        login_page.make_login_customer()

        customer_page = CustomerPage(login_page.driver)

        customer_page.is_url(), 'Aplicação não foi para página da cliente'