import allure

from pagesObject.HomePage import HomePage
from pagesObject.CartPage import CartPage
from pagesObject.SearchPage import SearchPage
from pagesObject.FicheProduitPage import FicheProduitPage

@allure.feature('Cart')
@allure.story('US-Cart')
@allure.description("Vérifie que l'application d'un code promo invalide affiche un message d'erreur")
def test_application_coupon_invalide(setup):
    """Vérifie que l'application d'un code promo invalide affiche un message d'erreur"""
    home_page = HomePage(setup)
    search_page = SearchPage(setup)
    ficheProduit_page = FicheProduitPage(setup)
    cart_page = CartPage(setup)

    with allure.step('ajouter produit au panier'):
        home_page.saisir_du_texte_dans_barre_de_recherche("MacBook")
        home_page.cliquer_sur_bouton_search()
        search_page.Ouvrir_fiche_produit("MacBook Pro")
        ficheProduit_page.cliquer_sur_add_to_cart()

    with allure.step('cliquer sur bouton panier'):
        home_page.cliquer_sur_le_bouton_panier()

    with allure.step('ajouter un code promo invalide'):
        cart_page.ajouter_un_code_promo("INVALIDCODE")
        cart_page.verifier_la_presence_message_code_coupon_invalide()
