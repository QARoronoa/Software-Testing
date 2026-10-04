from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pagesObject.BasePage import BasePage


class RegisterPage(BasePage):

    #locators
    champ_firstName = (By.ID, "input-firstname")
    champ_lastName = (By.ID, "input-lastname")
    champ_email = (By.ID, "input-email")
    champ_password = (By.ID, "input-password")
    champ_confirmPassword = (By.ID, "input-confirm")
    champ_telephone = (By.ID, "input-telephone")
    privacy_policy = (By.XPATH, "//label[@for='input-agree']")
    bouton_continue = (By.XPATH, "//input[@value='Continue']")
    alert_message_email_existant = (By.CSS_SELECTOR, ".alert-dismissible")
    message_erreur_champ_vide = (By.CSS_SELECTOR, ".text-danger")
    message_alerte_privacy_policy = (By.CSS_SELECTOR, ".alert-danger")


    def __init__(self, driver):
        super().__init__(driver)

    #methodes
    def remplir_le_formulaire(self, firstName, lastName, email, telephone, password, confirmPassword):
        self.saisir_du_texte(self.champ_firstName, firstName)
        self.saisir_du_texte(self.champ_lastName, lastName)
        self.saisir_du_texte(self.champ_email, email)
        self.saisir_du_texte(self.champ_telephone, telephone)
        self.saisir_du_texte(self.champ_password, password)
        self.saisir_du_texte(self.champ_confirmPassword, confirmPassword)

    def remplir_le_formulaire_mail_existant(self, firstName, lastName, email, telephone, password, confirmPassword):
        self.saisir_du_texte(self.champ_firstName, firstName)
        self.saisir_du_texte(self.champ_lastName, lastName)
        self.saisir_du_texte(self.champ_email, email)
        self.saisir_du_texte(self.champ_telephone, telephone)
        self.saisir_du_texte(self.champ_password, password)
        self.saisir_du_texte(self.champ_confirmPassword, confirmPassword)

    def remplir_le_formulaire_mdp_confirmation_different(self, firstName, lastName, email, telephone, password, confirmPassword):
        self.saisir_du_texte(self.champ_firstName, firstName)
        self.saisir_du_texte(self.champ_lastName, lastName)
        self.saisir_du_texte(self.champ_email, email)
        self.saisir_du_texte(self.champ_telephone, telephone)
        self.saisir_du_texte(self.champ_password, password)
        self.saisir_du_texte(self.champ_confirmPassword, confirmPassword)

    def cocher_case_privace_policy(self):
        case = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.privacy_policy))
        case.click()

    def cliquer_sur_continue(self):
        self.cliquer_sur_un_element(self.bouton_continue)

    def verifier_message_erreur_email_deja_existant(self):
        texte = self.capturer_le_texte_de_lelement(self.alert_message_email_existant)
        assert "already registered!" in texte

    def verifier_messages_derreurs_champs_vides(self):
        elements = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(self.message_erreur_champ_vide))
        assert len(elements) > 0
        for e in elements:
            print(e.text)

    def verifier_message_erreur_mdp_confirmation(self):
        texte = self.capturer_le_texte_de_lelement(self.message_erreur_champ_vide)
        assert texte == "Password confirmation does not match password!"

    def verifier_presence_message_alerte_privacy_policy(self):
        texte = self.capturer_le_texte_de_lelement(self.message_alerte_privacy_policy)
        assert texte == "Warning: You must agree to the Privacy Policy!"

    def verifier_message_erreur_wrong_message_or_password(self):
        texte = self.capturer_le_texte_de_lelement(self.message_alerte_privacy_policy)
        assert texte == "Warning: No match for E-Mail Address and/or Password."

    def verifier_message_erreur_champs_login_vides(self):
        texte = self.capturer_le_texte_de_lelement(self.message_alerte_privacy_policy)
        assert texte == "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."