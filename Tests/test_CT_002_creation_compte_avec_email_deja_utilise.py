import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.RegisterPage import RegisterPage

@allure.feature('Register')
@allure.story('US-REGISTER')
def test_creation_compte_avec_mail_existant(setup, remplir_form_mail_existant):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)


    with allure.step('Ouvrir register'):
        home_page.cliquer_sur_my_account()
        login_page.cliquer_sur_register()

    with allure.step('remplir formulaire'):
        register_page.remplir_le_formulaire(**remplir_form_mail_existant)

    with allure.step('cocher la case privacy Policy'):
        register_page.cocher_case_privace_policy()

    with allure.step('cliquer sur continue'):
        register_page.cliquer_sur_continue()

    with allure.step('message alerte est visible'):
        register_page.verifier_message_erreur_email_deja_existant()


