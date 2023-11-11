from pages.CustomerListPage import CustomerListPage


class TestCt5:

    def test_search_customer(self, manager_page):
        manager_page.click_aba_customers()

        customer_list_page = CustomerListPage(manager_page.driver)

        customer_list_page.is_url(), 'Aplicação não foi para página de clientes'

        customer_expected = ["Ron"]
        customer_list_page.search_customer("Ron")

        customers = customer_list_page.get_customers_in_table()

        assert customer_expected == customers, "Cliente Ron não foi filtrado em lista de clientes"
