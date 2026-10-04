import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.SearchPage import SearchPage
from pagesObject.FicheProduitPage import FicheProduitPage
from pagesObject.CartPage import CartPage

@allure.feature('Cart')
@allure.story('US-Cart')
def test_ajout_produit_panier(setup):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)
    ficheProduit_page = FicheProduitPage(setup)
    cart_page = CartPage(setup)


    with allure.step('saisir un article dans la barre de recherche'):
        home_page.saisir_du_texte_dans_barre_de_recherche("MacBook")

    with allure.step('cliquer sur le bouton search'):
        home_page.cliquer_sur_bouton_search()

    with allure.step('redirection vers la page search'):
        search_page.verifier_le_titre_de_la_page("Search - MacBook")

    with allure.step('Ouverture de la fiche produit'):
        search_page.Ouvrir_fiche_produit("MacBook Pro")

    with allure.step('cliquer sur add to cart'):
        ficheProduit_page.cliquer_sur_add_to_cart()

    with allure.step('cliquer sur bouton panier'):
        home_page.cliquer_sur_le_bouton_panier()

    with allure.step('Le produit est bien visible dans le panier'):
        cart_page.verifier_que_item_est_visible_dans_le_panier("MacBook Pro")

