import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.RegisterPage import RegisterPage

@allure.feature('Login')
@allure.story('US-LOGIN')
def test_connexion_avec_champs_vides(setup):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)

    with allure.step('clique sur myAccount'):
        home_page.cliquer_sur_my_account()

    with allure.step('se connecter'):
        login_page.remplir_le_champ_email('')
        login_page.remplir_le_champ_pwd('')
        login_page.cliquer_sur_login()

    with allure.step('message d erreur visible'):
        register_page.verifier_message_erreur_champs_login_vides()