from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pagesObject.BasePage import BasePage



class CheckoutPage(BasePage):

    #locators

    champ_first_name = (By.ID, "input-payment-firstname")
    champ_last_name = (By.ID, "input-payment-lastname")
    champ_address = (By.ID, "input-payment-address-1")
    champ_city = (By.ID, "input-payment-city")
    champ_post_code =(By.ID, "input-payment-postcode")
    champ_country = (By.ID, "input-payment-country")
    champ_region = (By.ID, "input-payment-zone")
    bouton_continue = (By.XPATH, "//button[text()='Continue ']")
    checkbox_terms_conditions = (By.XPATH, "(//select[@id='input-payment-zone'])")
    checkbox_privacy_conditions = (By.ID, "input-agree")
    bouton_confirm_order = (By.XPATH, "//button[text()='Confirm Order ']")
    alert_terms_conditions = (By.CSS_SELECTOR, ".alert-warning")

    def __init__(self, driver):
        super().__init__(driver)

    #methodes

    def remplir_le_formulaire(self, first_name, last_name, address, city, post_code):
        self.saisir_du_texte(self.champ_first_name, first_name)
        self.saisir_du_texte(self.champ_last_name, last_name)
        self.saisir_du_texte(self.champ_address, address)
        self.saisir_du_texte(self.champ_city, city)
        self.saisir_du_texte(self.champ_post_code, post_code)
        #choix country
        country_liste = Select(self.driver.find_element(*self.champ_country))
        country_liste.select_by_value("22")
        #choix region
        region_liste = Select(self.driver.find_element(*self.champ_region))
        region_liste.select_by_value("354")

    def cliquer_sur_continue(self):
        self.cliquer_sur_un_element(self.bouton_continue)

    def cocher_terms_conditions(self):
        self.cliquer_sur_un_element_js(self.checkbox_terms_conditions)
        self.cliquer_sur_un_element_js(self.checkbox_privacy_conditions)

    def cliquer_sur_confirm_oder(self):
        self.cliquer_sur_un_element(self.bouton_confirm_order)

    def verifier_la_presence_message_erreur(self):
        texte = self.capturer_le_texte_de_lelement(self.alert_terms_conditions)
        assert "Warning" in texte
        print(texte)