import allure
from pagesObject.HomePage import HomePage
from pagesObject.FicheProduitPage import FicheProduitPage
from pagesObject.LoginPage import LoginPage
from pagesObject.BrandPage import BrandPage
from pagesObject.WishListPage import WishListPage

@allure.feature('Wishlist')
@allure.story('US-WISHLIST')
@allure.description("Ajouter un article à ma wish list")
def test_Checkout_utilisateur_connecte_avec_formulaire_valide(setup, form_checkout):
    """Ajouter un article à ma wish list"""
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    brand_page = BrandPage(setup)
    wishList_page = WishListPage(setup)
    ficheProduit_page = FicheProduitPage(setup)


    with allure.step('se connecter'):
        home_page.cliquer_sur_my_account()
        login_page.remplir_le_champ_email('vremy@example.com')
        login_page.remplir_le_champ_pwd('Test123!')
        login_page.cliquer_sur_login()

    with allure.step('ouvrir fiche produit'):
        home_page.deplacer_curseur_sur_un_MENU("Mega Menu")
        home_page.cliquer_sur_un_sous_menu("Apple")
        brand_page.verifier_le_titre_de_la_page("Apple")
        brand_page.ouvrir_fiche_produit('Apple Cinema 30"')

    with allure.step("ajout produit à la wish list"):
        ficheProduit_page.deselectionner_favoris_si_necessaire()
        ficheProduit_page.cliquer_sur_le_bouton_favoris()
        home_page.cliquer_sur_voir_wishlist()


    with allure.step("redirection vers wishlist page "):
        wishList_page.verifier_le_titre_de_la_page("My Wish List")
        wishList_page.verifier_que_produit_est_present('Apple Cinema 30"')
