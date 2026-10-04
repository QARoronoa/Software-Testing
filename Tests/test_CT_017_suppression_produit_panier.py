import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.SearchPage import SearchPage
from pagesObject.FicheProduitPage import FicheProduitPage
from pagesObject.CartPage import CartPage

@allure.feature('Cart')
@allure.story('US-Cart')
def test_suppression_produit_panier(setup):
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

    with allure.step('suppression produit panier'):
        cart_page.cliquer_sur_bouton_suppression_quantite()


    with allure.step('message panier vide est visible'):
        cart_page.verifier_la_presence_message_panier_vide()
        time.sleep(4)