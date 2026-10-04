import pytest
from selenium import webdriver
from data.Register_data import registerData
from data.form_address import BillingAddress

@pytest.fixture(scope="function")
def setup(base_url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(base_url)

    yield driver
    driver.quit()

@pytest.fixture
def remplir_form_register():
    return registerData.form_register()

@pytest.fixture
def remplir_form_mail_existant():
    return registerData.form_register_failed()

@pytest.fixture
def remplir_form_mdp_different():
    return registerData.form_register_mdp_different()

@pytest.fixture
def form_checkout():
    return BillingAddress.formulaire_adress()
