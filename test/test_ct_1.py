import pytest

from pages.PageAddCustomer import PageAddCustomer

class TestCt1:

        def test_add_customer(self, manager_page):
                manager_page.click_aba_add_customer()
                pageAddCustomer = PageAddCustomer(driver=manager_page.driver)
                pageAddCustomer.is_url(), 'Aplicação não foi para página de adicionar cliente'
                pageAddCustomer.insert_customer_data()
                text_alert = pageAddCustomer.click_add_customer_btn()
                assert text_alert.startswith('Customer added successfully')
