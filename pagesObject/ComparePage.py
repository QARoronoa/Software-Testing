from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pagesObject.BasePage import BasePage

class ComparePage(BasePage):

    #locators
    bouton_remove = (By.LINK_TEXT, "Remove")
    message_aucun_produit_compare = (By.XPATH, "//p[normalize-space()='You have not chosen any products to compare.']")

    def __init__(self,driver):
        super().__init__(driver)

    #methodes

    def cliquer_sur_les_boutons_remove(self):
        boutons_remove = self.driver.find_elements(*self.bouton_remove)

        for i in range(len(boutons_remove)):
            bouton = self.driver.find_element(*self.bouton_remove)
            bouton.click()

    def verifier_que_la_page_comparaison_est_vide(self):
       message =  self.capturer_le_texte_de_lelement(self.message_aucun_produit_compare)
       assert "any products to compare" in message