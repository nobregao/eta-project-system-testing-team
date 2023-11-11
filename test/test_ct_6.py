from datetime import datetime

from model.Customer import Customer
from pages.CustomerListPage import CustomerListPage
from pages.PageAddCustomer import PageAddCustomer


class TestCT6:

    def test_delete_customer(self, manager_page):

        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        customer_for_delete = Customer("Cliente "+datetime_now, "Teste", "12345-000")

        # adicionando cliente
        manager_page.click_aba_add_customer()

        page_add_customer = PageAddCustomer(driver=manager_page.driver)
        page_add_customer.insert_customer_data(
            customer_for_delete.first_name,
            customer_for_delete.last_name,
            customer_for_delete.post_code
        )
        page_add_customer.click_add_customer_btn()

        # removendo cliente adicionado
        manager_page.click_aba_customers()

        customer_list_page = CustomerListPage(manager_page.driver)

        customer_list_page.is_url(), 'Aplicação não foi para página de clientes'

        customer_list_page.delete_customer(customer_for_delete.first_name)

        customers_after = customer_list_page.get_customers_in_table()

        assert customer_for_delete.first_name not in customers_after, "Cliente {} não foi deletado da lista".format(customer_for_delete.first_name)