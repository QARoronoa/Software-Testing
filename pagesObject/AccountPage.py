from selenium.webdriver.common.by import By

from pagesObject.BasePage import BasePage

class AccountPage(BasePage):

    #locators
    logo_lambtatest = (By.XPATH, '//a[@title="Poco Electro"]')

    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def cliquer_sur_le_bouton_homePage(self):
        self.cliquer_sur_un_element(self.logo_lambtatest)