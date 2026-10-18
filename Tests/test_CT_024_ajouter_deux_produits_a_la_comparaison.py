import allure
from pagesObject.HomePage import HomePage
from pagesObject.FicheProduitPage import FicheProduitPage
from pagesObject.BrandPage import BrandPage
from pagesObject.ComparePage import ComparePage


@allure.feature('Compare')
@allure.story('US-COMPARE')
@allure.description("Ajouter deux produits à la comparaison")
def test_Ajouter_deux_produits_a_la_comparaison(setup):
    """Ajouter deux produits à la comparaison"""
    home_page = HomePage(setup)
    brand_page = BrandPage(setup)
    ficheProduit_page = FicheProduitPage(setup)
    compare_page = ComparePage(setup)


    with allure.step('ouvrir fiche produit et clique sur compare'):
        home_page.deplacer_curseur_sur_un_MENU("Mega Menu")
        home_page.cliquer_sur_un_sous_menu("Apple")
        brand_page.verifier_le_titre_de_la_page("Apple")
        brand_page.ouvrir_fiche_produit('Apple Cinema 30"')
        ficheProduit_page.cliquer_sur_bouton_compare()

    with allure.step('ouvrir fiche produit numero 2 et clique sur compare'):
        home_page.deplacer_curseur_sur_un_MENU("Mega Menu")
        home_page.cliquer_sur_un_sous_menu("Apple")
        brand_page.verifier_le_titre_de_la_page("Apple")
        brand_page.ouvrir_fiche_produit('MacBook Pro')
        ficheProduit_page.cliquer_sur_bouton_compare()

    with allure.step('clique sur le bouton compare'):
        ficheProduit_page.cliquer_sur_bouton_compare_popin()
        ficheProduit_page.verifier_le_titre_de_la_page("Product Comparison")

    with allure.step('supprimer les articles de la page comparaison'):
        compare_page.cliquer_sur_les_boutons_remove()
        compare_page.verifier_que_la_page_comparaison_est_vide()

