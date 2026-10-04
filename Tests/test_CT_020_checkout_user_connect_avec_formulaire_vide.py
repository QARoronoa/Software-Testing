import time

import allure
import pytest

from pagesObject.HomePage import HomePage
from pagesObject.CartPage import CartPage
from pagesObject.SearchPage import SearchPage
from pagesObject.FicheProduitPage import FicheProduitPage
from pagesObject.LoginPage import LoginPage
from pagesObject.CheckoutPage import CheckoutPage

pytest.mark.skip("test incomplet")

@allure.feature('Checkout')
@allure.story('US-Checkout')
@allure.description("Utilisateur connecté et produit dans panier")
def test_Checkout_utilisateur_connecte_avec_formulaire_valide(setup, form_checkout):
    """Utilisateur connecté et produit dans panier"""
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    search_page = SearchPage(setup)
    ficheProduit_page = FicheProduitPage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)

    with allure.step('se connecter'):
        home_page.cliquer_sur_my_account()
        login_page.remplir_le_champ_email('vremy@example.com')
        login_page.remplir_le_champ_pwd('Test123!')
        login_page.cliquer_sur_login()

    with allure.step('ajouter produit au panier'):
        home_page.saisir_du_texte_dans_barre_de_recherche("MacBook")
        home_page.cliquer_sur_bouton_search()
        search_page.Ouvrir_fiche_produit("MacBook Pro")
        ficheProduit_page.cliquer_sur_add_to_cart()
        ficheProduit_page.ouvrir_panier()

    with allure.step('faire le checkout'):
        cart_page.cliquer_sur_le_bouton_checkout()

    with allure.step('remplir le formulaire'):
        checkout_page.remplir_le_formulaire(**form_checkout)
        checkout_page.cocher_terms_conditions()
        checkout_page.cliquer_sur_continue()

    with allure.step('valider la commande'):
        checkout_page.cliquer_sur_confirm_oder()



        time.sleep(5)