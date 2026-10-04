import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.CartPage import CartPage
from pagesObject.SearchPage import SearchPage
from pagesObject.FicheProduitPage import FicheProduitPage
from pagesObject.LoginPage import LoginPage
from pagesObject.CheckoutPage import CheckoutPage

@allure.feature('Checkout')
@allure.story('US-Checkout')
@allure.description("Checkout avec champs obligatoires manquants")
def test_Checkout_utilisateur_connecte_avec_formulaire_valide(setup, form_checkout):
    """Checkout avec champs obligatoires manquants"""
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
        ficheProduit_page.cliquer_sur_view_cart()

    with allure.step('faire le checkout'):
        cart_page.cliquer_sur_le_bouton_checkout()
        cart_page.cliquer_sur_le_bouton_continue()
        checkout_page.verifier_la_presence_message_erreur()
