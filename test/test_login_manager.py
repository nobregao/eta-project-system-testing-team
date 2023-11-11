from pages.ManagerPage import ManagerPage


class TestLoginManager:

    def test_make_login_manager(self, login_page):

        login_page.make_login_manager()

        customer_page = ManagerPage(login_page.driver)

        customer_page.is_url(), 'Aplicação não foi para página da gerente'
