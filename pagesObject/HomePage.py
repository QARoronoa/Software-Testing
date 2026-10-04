import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pagesObject.BasePage import BasePage


class HomePage(BasePage):

    # locators
    myAccount_bouton = (By.XPATH, "//span[normalize-space()='My account']")
    barre_de_recherche = (By.XPATH,"//input[@name='search']")
    bouton_search = (By.XPATH,"//button[text()='Search']")
    bouton_panier = (By.XPATH, "(//div[@class='cart-icon'])[1]")
    bouton_edit_cart = (By.LINK_TEXT, "Edit cart")


    def __init__(self, driver):
        super().__init__(driver)

    #methodes
    def cliquer_sur_my_account(self):
        self.cliquer_sur_un_element_js(self.myAccount_bouton)

    def saisir_du_texte_dans_barre_de_recherche(self, item):
        self.saisir_du_texte(self.barre_de_recherche, item)

    def cliquer_sur_bouton_search(self):
        self.cliquer_sur_un_element(self.bouton_search)

    def cliquer_sur_le_bouton_panier(self):
        self.cliquer_sur_un_element(self.bouton_panier)
        self.cliquer_sur_un_element(self.bouton_edit_cart)