import allure
from pagesObject.HomePage import HomePage
from pagesObject.SearchPage import SearchPage
from pagesObject.FicheProduitPage import FicheProduitPage

@allure.feature('Product')
@allure.story('US-PRODUCT')
def test_modifier_fiche_quantite_dans_fiche_produit(setup):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)
    ficheProduit_page = FicheProduitPage(setup)


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

    with allure.step('Modification quantite à 2'):
        ficheProduit_page.Augmenter_quantite_produit()

    with allure.step('cliquer sur add to cart'):
        ficheProduit_page.cliquer_sur_add_to_cart()

