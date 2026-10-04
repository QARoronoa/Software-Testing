from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pagesObject.BasePage import BasePage

class CartPage(BasePage):

    #locators
    nom_item = (By.CSS_SELECTOR, ".text-left a")
    champ_quantite = (By.XPATH, "//input[contains(@name,'quantity')]")
    bouton_update_quantite = (By.CSS_SELECTOR, ".fa-sync-alt")
    bouton_supprimer_quantite = (By.CSS_SELECTOR, ".btn-danger")
    alerte_message_update = (By.CSS_SELECTOR, ".alert-dismissible")
    message_panier_vide = (By.XPATH, "//p[normalize-space()='Your shopping cart is empty!']")
    bouton_continue = (By.ID, "button-save")
    bouton_coupon_code = (By.XPATH, "//h5[normalize-space()='Use Coupon Code']")
    champ_coupon = (By.ID, "input-coupon")
    bouton_apply_code = (By.ID, "button-coupon")
    message_coupon_invalide = (By.CSS_SELECTOR, ".alert-dismissible")
    bouton_checkout = (By.LINK_TEXT, "Checkout")




    def __init__(self, driver):
        super().__init__(driver)

    def verifier_que_item_est_visible_dans_le_panier(self, nom_article_attendu):
        titre_item = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.nom_item))
        nom_article = titre_item.text
        assert nom_article == nom_article_attendu

    def modifier_quantite_article(self, nombre):
       self.saisir_du_texte(self.champ_quantite, nombre)

    def cliquer_sur_le_bouton_rafraichir(self):
        self.cliquer_sur_un_element(self.bouton_update_quantite)

    def verifier_mise_a_jour_quantite(self):
        mess = self.capturer_le_texte_de_lelement(self. alerte_message_update)
        assert "Success" in mess

    def cliquer_sur_bouton_suppression_quantite(self):
        self.cliquer_sur_un_element(self.bouton_supprimer_quantite)

    def verifier_la_presence_message_panier_vide(self):
        # mess = self.capturer_le_texte_de_lelement(self.message_panier_vide)
        # assert "empty" in mess
        bouton = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.bouton_continue))

    def ajouter_un_code_promo(self, code):
        self.cliquer_sur_un_element(self.bouton_coupon_code)
        self.saisir_du_texte(self.champ_coupon, code)
        self.cliquer_sur_un_element(self.bouton_apply_code)

    def verifier_la_presence_message_code_coupon_invalide(self):
        messa = self.capturer_le_texte_de_lelement(self.message_coupon_invalide)
        assert "Coupon is either invalid," in messa

    def cliquer_sur_le_bouton_checkout(self):
        self.cliquer_sur_un_element(self.bouton_checkout)

    def cliquer_sur_le_bouton_continue(self):
        self.cliquer_sur_un_element(self.bouton_continue)