import time

import allure
from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.RegisterPage import RegisterPage

@allure.feature('Login')
@allure.story('US-LOGIN')
def test_connexion_avec_identifiant_valides(setup):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)

    with allure.step('clique sur myAccount'):
        home_page.cliquer_sur_my_account()

    with allure.step('se connecter'):
        login_page.remplir_le_champ_email('vremy@example.com')
        login_page.remplir_le_champ_pwd('Test123!')
        login_page.cliquer_sur_login()

    with allure.step('redirection vers la page my account'):
        login_page.verifier_le_titre_de_la_page('My Account')


