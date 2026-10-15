import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.FicheProduitPage import FicheProduitPage
from pagesObject.LoginPage import LoginPage
from pagesObject.BrandPage import BrandPage
from pagesObject.WishListPage import WishListPage

@allure.feature('Wishlist')
@allure.story('US-WISHLIST')
@allure.description("Ajouter un article à ma wish list user non connecté")
def test_Checkout_utilisateur_non_connecte_ajoute_article_wishList(setup):
    """Ajouter un article à ma wish list user non connecté"""
    home_page = HomePage(setup)
    brand_page = BrandPage(setup)
    ficheProduit_page = FicheProduitPage(setup)


    with allure.step('ouvrir fiche produit'):
        home_page.deplacer_curseur_sur_un_MENU("Mega Menu")
        home_page.cliquer_sur_un_sous_menu("Apple")
        brand_page.verifier_le_titre_de_la_page("Apple")
        brand_page.ouvrir_fiche_produit('Apple Cinema 30"')

    with allure.step("ajout produit à la wish list"):
        ficheProduit_page.cliquer_sur_le_bouton_favoris()

    with allure.step('ouverture popin connexion ou register'):
        ficheProduit_page.verifier_la_presence_popin_login()
