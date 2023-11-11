from datetime import datetime

from model.Customer import Customer
from pages.CustomerListPage import CustomerListPage
from pages.PageAddCustomer import PageAddCustomer


class TestCt3:

    def test_customer_is_on_the_list(self, manager_page):
        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        customer_for_exist = Customer("Cliente " + datetime_now, "Teste", "12345-000")

        # adicionando cliente
        manager_page.click_aba_add_customer()

        page_add_customer = PageAddCustomer(driver=manager_page.driver)
        page_add_customer.insert_customer_data(
            customer_for_exist.first_name,
            customer_for_exist.last_name,
            customer_for_exist.post_code
        )
        page_add_customer.click_add_customer_btn()
        manager_page.click_aba_customers()
        customer_list_page = CustomerListPage(manager_page.driver)
        customer_list_page.is_url(), 'Aplicação não foi para página de clientes'
        customers = customer_list_page.get_customers_in_table()

        assert customer_for_exist.first_name in customers, 'Cliente não encontrado!'
