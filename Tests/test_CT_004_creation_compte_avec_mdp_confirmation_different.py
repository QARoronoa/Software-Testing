import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.RegisterPage import RegisterPage

@allure.feature('Register')
@allure.story('US-REGISTER')
def test_creation_compte_avec_mdp_confirmation_different(setup, remplir_form_mdp_different):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)

    with allure.step('Ouvrir register'):
        home_page.cliquer_sur_my_account()
        login_page.cliquer_sur_register()

    with allure.step('remplir formulaire'):
        register_page.remplir_le_formulaire_mdp_confirmation_different(**remplir_form_mdp_different)

    with allure.step('cocher privacy policy'):
        register_page.cocher_case_privace_policy()

    with allure.step('cliquer sur le bouton Continue'):
        register_page.cliquer_sur_continue()

    with allure.step('le message derreur mdp confirmation est visible'):
        register_page.verifier_message_erreur_mdp_confirmation()

