import allure
from pagesObject.HomePage import HomePage
from pagesObject.CartPage import CartPage
from pagesObject.SearchPage import SearchPage
from pagesObject.FicheProduitPage import FicheProduitPage

@allure.feature('Checkout')
@allure.story('US-Checkout')
@allure.description("Accéder au checkout depuis le panier")
def test_application_coupon_invalide(setup):
    """Accéder au checkout depuis le panier"""
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

    with allure.step('cliquer sur le bouton checkout'):
        cart_page.cliquer_sur_le_bouton_checkout()
        cart_page.verifier_le_titre_de_la_page('Checkout')
