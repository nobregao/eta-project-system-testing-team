from selenium.webdriver.common.alert import Alert

from pages.PageCreateAccount import PageCreateAccount


class TestCt2:

    def test_open_account_sucess(self, manager_page):
        manager_page.click_aba_open_account()

        page_create_account = PageCreateAccount(driver=manager_page.driver)
        page_create_account.is_url(), 'Aplicação não foi para página de criação de conta'
        page_create_account.select_customer_name('Harry Potter')
        page_create_account.select_currency('Dollar')
        page_create_account.click_process_btn()

        alert = Alert(page_create_account.driver)
        assert alert.text.startswith('Account created successfully')
