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

class tratare_add_uri(unittest.TestCase):

    TEXT_ADD = (By. XPATH,"//div[@class='modal-body']/p")
    TEXT_TITLU = (By. XPATH, "//div[@class='modal-title']/h3")
    CLOSE_BUTTON = (By. XPATH, "//div[@class='modal-footer']/p")
    TITLU_PAGINA_DESCHISA = (By. XPATH, "//div[@class='example']/h3")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/entry_ad")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    # Verificare mesaj add cand accesam linkul
    def test_mesaj_add(self):
        time.sleep (1)
        text_afisat_add = self.chrome.find_element(*self.TEXT_ADD).text
        text_asteptat_add = "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker)."
        assert text_afisat_add == text_asteptat_add, f"ERROR: Expected: {text_asteptat_add}, ACTUAL: {text_afisat_add}"

    # Verificare titlul add-ului cand accesam linkul
    def test_text_titlu_add(self):
        time.sleep(1)
        nume_titlu_afisat_add = self.chrome.find_element(*self.TEXT_TITLU).text
        nume_titlu_asteptat_add = "THIS IS A MODAL WINDOW"
        assert nume_titlu_afisat_add == nume_titlu_asteptat_add, f"ERROR: Expected: {nume_titlu_asteptat_add}, ACTUAL: {nume_titlu_afisat_add}"


    # Apasare buton CLOSE cand apare add-ul
    def test_closed_add(self):
        time.sleep(1)
        self.chrome.find_element(*self.CLOSE_BUTTON).click()
        text_titlul_paginii = self.chrome.find_element(*self.TITLU_PAGINA_DESCHISA).text
        text_titlul_paginii_asteptat = "Entry Ad"
        assert text_titlul_paginii == text_titlul_paginii_asteptat, f"ERROR: Expected: {text_titlul_paginii_asteptat}, ACTUAL: {text_titlul_paginii}"


