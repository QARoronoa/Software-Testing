from selenium.webdriver.common.by import By

from pagesObject.BasePage import BasePage


class FicheProduitPage(BasePage):

    #locators
    bouton_increase_quantity = (By.XPATH, '(//button[@aria-label="Increase quantity"])[2]')
    bouton_add_to_cart = (By.XPATH, "(//button[text()='Add to Cart'])[2]")
    bouton_panier = (By.XPATH, '(//div[@class="cart-icon"])[1]')
    bouton_view_cart = (By.LINK_TEXT, "View Cart")
    bouton_checkout = (By.LINK_TEXT, "Checkout ")
    bouton_wishlist = (By.XPATH, "(//button[@class='btn btn-wishlist wishlist-42' ])[1]")
    bouton_wishlist_selectionne = (By.XPATH, '(//button[@class="btn btn-wishlist wishlist-42 wished"])[1]')
    bouton_wishList_popin = (By.XPATH, "//a[normalize-space()='Wish List (1)']")


    def __init__(self, driver):
        super().__init__(driver)

    #methodes

    def Augmenter_quantite_produit(self):
        self.cliquer_sur_un_element(self.bouton_increase_quantity)

    def cliquer_sur_add_to_cart(self):
        self.cliquer_sur_un_element(self.bouton_add_to_cart)

    def cliquer_sur_le_bouton_checkout(self):
        self.cliquer_sur_un_element(self.bouton_checkout)

    def ouvrir_panier(self):
        self.cliquer_sur_un_element(self.bouton_panier)

    def cliquer_sur_view_cart(self):
        self.cliquer_sur_un_element(self.bouton_view_cart)

    def cliquer_sur_le_bouton_favoris(self):
        self.cliquer_sur_un_element_js(self.bouton_wishlist)

    def deselectionner_favoris_si_necessaire(self):
        boutons = self.driver.find_elements(*self.bouton_wishlist_selectionne)
        if boutons:
            self.cliquer_sur_un_element(self.bouton_wishlist_selectionne)

