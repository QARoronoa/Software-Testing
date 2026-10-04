import time

import allure

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.RegisterPage import RegisterPage

@allure.feature('Register')
@allure.story('US-REGISTER')
def test_creation_compte(setup, remplir_form_register):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)

    with allure.step('cliquer sur my account'):
        home_page.cliquer_sur_my_account()

    with allure.step('redirection vers la page register'):
        login_page.verifier_le_titre_de_la_page("Account Login")

    with allure.step('cliquer sur register'):
        login_page.cliquer_sur_register()

    with allure.step('remplir le formulaire dinscription'):
        register_page.remplir_le_formulaire(**remplir_form_register)

    with allure.step('cocher la case privacy Policy'):
        register_page.cocher_case_privace_policy()

    with allure.step('cliquer sur continue'):
        register_page.cliquer_sur_continue()

    with allure.step('redirection vers la page compte créé'):
        register_page.verifier_le_titre_de_la_page("Your Account Has Been Created!")

