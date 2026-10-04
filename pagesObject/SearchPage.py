from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pagesObject.BasePage import BasePage



class SearchPage(BasePage):

    #locators
    message_item_inexistant = (By.CSS_SELECTOR, ".content-products p")


    def __init__(self, driver):
        super().__init__(driver)

    #methodes
    def verifier_message_produits_inexistant(self):
        texte = self.capturer_le_texte_de_lelement(self.message_item_inexistant)
        assert "There is no product that matches the search criteria." in texte
        print(texte)

    def Ouvrir_fiche_produit(self, nom_produit):
        produit = (By.LINK_TEXT, nom_produit)
        element_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(produit))
        element_link.click()
