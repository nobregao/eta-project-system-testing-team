from pages.Page import Page


class CustomerPage(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"

    def __init__(self, driver):
        super().__init__(self.url, driver)

