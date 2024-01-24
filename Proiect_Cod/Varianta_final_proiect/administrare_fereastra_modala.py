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

class administrare_fereastra_modala(unittest.TestCase):

    COMPONENTE = (By.ID, 'navbarDropdownMenuLink')
    MODAL = (By.XPATH, '// *[contains( @class ,"dropdown-item")][10]')
    OPENMODAL = (By.ID, 'modal-button')
    TEXT_AFISAT_MODAL = (By.XPATH, '// *[contains( @class ,"modal-body")]')
    PATHMODAL = (By.XPATH, "//div[@class='modal-content']/div[2]")
    TITLU_MESAJ_MODAL = (By.XPATH, "//div[@class='modal-header']/h5")
    OK_BUTTON = (By. ID, "ok-button")
    CLOSE_BUTTON = (By. ID, "close-button")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    # Verificare mesaj cand apasam butonul modal
    def test_mesaj_modal(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.MODAL).click()
        self.chrome.find_element(*self.OPENMODAL).click()
        time.sleep(1)
        text_modal = self.chrome.find_element(*self.PATHMODAL).text
        text_modal_expected = "Some text here"
        assert text_modal == text_modal_expected, f"ERROR: Expected: {text_modal_expected}, ACTUAL: {text_modal}"

    # Verificare titlu cand apasam butonul modal
    def test_text_titlu_modal(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.MODAL).click()
        self.chrome.find_element(*self.OPENMODAL).click()
        time.sleep(1)
        text_titlu_modal = self.chrome.find_element(*self.TITLU_MESAJ_MODAL).text
        text_titlu_modal_expected = "Modal title"
        assert text_titlu_modal == text_titlu_modal_expected, f"ERROR: Expected: {text_titlu_modal_expected}, ACTUAL: {text_titlu_modal}"

    # Apasare buton OK cand fereastra modal deshisa
    def test_apasare_buton_ok(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.MODAL).click()
        self.chrome.find_element(*self.OPENMODAL).click()
        time.sleep(1)
        self.chrome.find_element(*self.OK_BUTTON).click()
        text_modal = self.chrome.find_element(*self.PATHMODAL).text
        text_modal_expected = "Some text here"
        assert text_modal == text_modal_expected, f"ERROR: Expected: {text_modal_expected}, ACTUAL: {text_modal}"

    # Apasare buton CLOSE cand fereastra modal deshisa
    def test_apasare_buton_closed(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.MODAL).click()
        self.chrome.find_element(*self.OPENMODAL).click()
        time.sleep(1)
        self.chrome.find_element(*self.CLOSE_BUTTON).click()
        nume_buton_modal = self.chrome.find_element(*self.OPENMODAL).text
        nume_buton_modal_expected = "Open modal"
        assert nume_buton_modal == nume_buton_modal_expected, f"ERROR: Expected: {nume_buton_modal_expected}, ACTUAL: {nume_buton_modal}"


