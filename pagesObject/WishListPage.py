from selenium.webdriver.common.by import By

from pagesObject.BasePage import BasePage


class WishListPage(BasePage):

    #locators
    bouton_remove = (By.XPATH, "//a[@data-original-title='Remove']")


    def __init__(self, driver):
        super().__init__(driver)

    #methodes

    def verifier_que_produit_est_present(self, item):
        product_name = (By.LINK_TEXT, item)
        nom_item = self.capturer_le_texte_de_lelement(product_name)
        assert nom_item == item

    def vider_la_wishList(self):
        item = (By.XPATH, '//img[@title=\'Apple Cinema 30"\']')
        if len(self.driver.find_elements(*item)) > 0:
            self.cliquer_sur_un_element(self.bouton_remove)


    def supprimer_le_produit_de_la_wishList(self):
        self.cliquer_sur_un_element(self.bouton_remove)

