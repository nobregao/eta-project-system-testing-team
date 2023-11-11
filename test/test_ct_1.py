from pages.PageAddCustomer import PageAddCustomer


class TestCt1:

        def test_add_customer(self, manager_page):
                manager_page.click_aba_add_customer()

                page_add_customer = PageAddCustomer(driver=manager_page.driver)
                page_add_customer.is_url(), 'Aplicação não foi para página de adicionar cliente'
                page_add_customer.insert_customer_data()

                text_alert = page_add_customer.click_add_customer_btn()
                assert text_alert.startswith('Customer added successfully')
