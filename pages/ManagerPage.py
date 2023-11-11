from pages.Page import Page


class ManagerPage(Page):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, driver):
        super().__init__(self.url, driver)

