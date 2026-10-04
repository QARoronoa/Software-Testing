import allure
from pagesObject.HomePage import HomePage
from pagesObject.SearchPage import SearchPage

@allure.feature('Search')
@allure.story('US-SEARCH')
def test_recherche_produit_inexistant(setup):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)


    with allure.step('saisir un article dans la barre de recherche'):
        home_page.saisir_du_texte_dans_barre_de_recherche("prout")

    with allure.step('cliquer sur le bouton search'):
        home_page.cliquer_sur_bouton_search()

    with allure.step('Message produits inexistant visible'):
        search_page.verifier_message_produits_inexistant()
