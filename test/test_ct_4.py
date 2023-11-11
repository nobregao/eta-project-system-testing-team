from pages.CustomerListPage import CustomerListPage


class TestCT4:

    def test_sort_customer(self, manager_page):
        manager_page.click_aba_customers()

        customer_list_page = CustomerListPage(manager_page.driver)

        customer_list_page.is_url(), 'Aplicação não foi para página de clientes'

        customer_list_before = customer_list_page.get_customers_in_table()
        customer_list_expected = sorted(customer_list_before)

        customer_list_page.sort_table_for_first_name_alphabetically()

        customer_list_after = customer_list_page.get_customers_in_table()

        assert customer_list_expected == customer_list_after, "Clientes não foram ordenados pelo campo 'First Name'"
