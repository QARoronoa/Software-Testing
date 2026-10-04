import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.SearchPage import SearchPage

@allure.feature('Product')
@allure.story('US-PRODUCT')
def test_ouvrir_fiche_produit_depuis_resultat_recherhe(setup):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)


    with allure.step('saisir un article dans la barre de recherche'):
        home_page.saisir_du_texte_dans_barre_de_recherche("MacBook")

    with allure.step('cliquer sur le bouton search'):
        home_page.cliquer_sur_bouton_search()

    with allure.step('redirection vers la page search'):
        search_page.verifier_le_titre_de_la_page("Search - MacBook")

    with allure.step('Ouverture de la fiche produit'):
        search_page.Ouvrir_fiche_produit("MacBook Pro")

    with allure.step('verifier redirection vers la fiche du produit'):
        search_page.verifier_le_titre_de_la_page("MacBook Pro")

