from selenium.webdriver.common.by import By

from pagesObject.BasePage import BasePage


class LoginPage(BasePage):

    #locators
    link_register = (By.LINK_TEXT, "Register")
    champ_email = (By.ID, "input-email")
    champ_password = (By.ID, "input-password")
    bouton_login = (By.XPATH, "//input[@value='Login']")
    bouton_logout = (By.LINK_TEXT, "Logout")
    titre_account_logout = (By.CSS_SELECTOR, ".my-3")



    def __init__(self, driver):
        super().__init__(driver)

    #methodes

    def cliquer_sur_register(self):
        self.cliquer_sur_un_element(self.link_register)

    def remplir_le_champ_email(self, email):
        self.saisir_du_texte(self.champ_email, email)

    def remplir_le_champ_pwd(self, password):
        self.saisir_du_texte(self.champ_password, password)

    def cliquer_sur_login(self):
        self.cliquer_sur_un_element(self.bouton_login)

    def cliquer_sur_logout(self):
        self.cliquer_sur_un_element(self.bouton_logout)

    def verifier_la_deconnexion(self):
        text = self.capturer_le_texte_de_lelement(self.titre_account_logout)
        assert "Account Logout" in text
