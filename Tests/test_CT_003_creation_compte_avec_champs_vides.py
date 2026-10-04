import allure
from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.RegisterPage import RegisterPage

@allure.feature('Register')
@allure.story('US-REGISTER')
def test_creation_compte_avec_mail_existant(setup):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)

    with allure.step('Ouvrir register'):
        home_page.cliquer_sur_my_account()
        login_page.cliquer_sur_register()

    with allure.step('cocher privacy policy'):
        register_page.cocher_case_privace_policy()

    with allure.step('cliquer sur le bouton Continue'):
        register_page.cliquer_sur_continue()

    with allure.step('les messages d\'alertes sont visibles'):
        register_page.verifier_messages_derreurs_champs_vides()
