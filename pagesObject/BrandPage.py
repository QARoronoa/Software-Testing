from selenium.webdriver.common.by import By

from pagesObject.BasePage import BasePage


class BrandPage(BasePage):

    #locators


    #methodes



    def __init__(self, driver):
        super().__init__(driver)


    def ouvrir_fiche_produit(self, nom_produit):
        produit = (By.XPATH, f"//a[normalize-space()='{nom_produit}']")
        self.cliquer_sur_un_element(produit)

