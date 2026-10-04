import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver =driver

    @allure.step('clique sur l element {locator}')
    def cliquer_sur_un_element(self, locator):
        element=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        element.click()

    @allure.step('text saisi {text}')
    def saisir_du_texte(self, locator, text):
        element=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def cliquer_sur_un_element_js(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        self.driver.execute_script("arguments[0].click();",element)

    @allure.step("le titre de la page est {titre_attendu}")
    def verifier_le_titre_de_la_page(self, titre_attendu):
        titre= self.driver.title
        assert titre_attendu == titre, f"titre obtenu {titre}, titre attendu {titre_attendu}"


    def capturer_le_texte_de_lelement(self,locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        texte_element = element.text
        with allure.step(f"le texte de l'element est {texte_element}"):
            pass
            return texte_element
