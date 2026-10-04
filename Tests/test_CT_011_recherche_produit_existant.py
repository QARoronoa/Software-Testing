import allure
from pagesObject.HomePage import HomePage
from pagesObject.SearchPage import SearchPage

@allure.feature('Search')
@allure.story('US-SEARCH')
def test_recherche_produit_existant(setup):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)


    with allure.step('saisir un article dans la barre de recherche'):
        home_page.saisir_du_texte_dans_barre_de_recherche("MacBook")

    with allure.step('cliquer sur le bouton search'):
        home_page.cliquer_sur_bouton_search()

    with allure.step('redirection vers la page search'):
        search_page.verifier_le_titre_de_la_page("Search - MacBook")
