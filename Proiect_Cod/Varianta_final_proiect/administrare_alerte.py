from time import sleep
import time
from datetime import date
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class administrare_alerte(unittest.TestCase):

    COMPONENTE = (By.ID, 'navbarDropdownMenuLink')
    SWITCH_WINDOW = (By.XPATH, '//*[text()="Switch Window"][1]')
    ALERTA = (By.ID, 'alert-button')
    TEXT_ALERTA = (By.XPATH, "//div[@class='form-group row']/script")
    OPEN_NEW_TAB = (By.ID, 'new-tab-button')
    WELLCOME_TO_NEW_PAGE = (By.XPATH, "//div[@class = 'container']/div/h1")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    # Verificare buton alerta si acceptare alerta
    def test_verificare_buton_alerta_si_acceptare_alerta(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.SWITCH_WINDOW).click()
        self.chrome.find_element(*self.ALERTA).click()
        buton_alerta = self.chrome.switch_to.alert
        buton_alerta.accept()

        text_buton_alerta = self.chrome.find_element(*self.ALERTA).text
        expected_buton_alerta = "Open alert"
        assert text_buton_alerta == expected_buton_alerta, f"ERROR: Expected: {expected_buton_alerta}, ACTUAL: {text_buton_alerta}"

    # Verificare buton alerta si alerta denied
    def test_verificare_buton_alerta_negare_alerta(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.SWITCH_WINDOW).click()
        self.chrome.find_element(*self.ALERTA).click()
        buton_alerta = self.chrome.switch_to.alert
        buton_alerta.dismiss()

        text_buton_alerta = self.chrome.find_element(*self.ALERTA).text
        expected_buton_alerta = "Open alert"
        assert text_buton_alerta == expected_buton_alerta, f"ERROR: Expected: {expected_buton_alerta}, ACTUAL: {text_buton_alerta}"

    # Verificare accesare pagina noua prin verificarea numarului de tab uri deschise
    def test_new_window(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.SWITCH_WINDOW).click()
        self.chrome.find_element(*self.OPEN_NEW_TAB).click()
        assert len(self.chrome.window_handles) == 2, f"ERROR: Numarul de ferestre deschise nu este 2"



