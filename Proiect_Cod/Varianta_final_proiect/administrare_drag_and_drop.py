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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class administrare_drag_and_drop(unittest.TestCase):
    COMPONENTE = (By.ID, 'navbarDropdownMenuLink')
    DRAGDROP = (By.XPATH, '//*[text()="Drag and Drop"]')
    IMAGE_TO_DRAG = (By. XPATH, "//img[@src='/assets/selenium-logo-c1d6f4654a0c8f8bef745f71b4e22836224aabc2116f405ef511cd79c48f2947.png']")
    PLACE_TO_DROP = (By. XPATH,"//*[@class = 'ui-widget-header']/p")
    PATH_TEXT_AFISARE_DROP = (By. XPATH, '//*[@class ="ui-widget-header ui-droppable ui-state-highlight"]')
    TEXT_TITLU_PATH = (By. XPATH, "//*[@class ='container']/h1")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    # Verificarea rularii operatiunii de drag and drop
    def test_drag_drop(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.DRAGDROP).click()
        time.sleep(3)
        # path pentru elementul sursa
        drag_from = WebDriverWait(self.chrome, 5).until(EC.element_to_be_clickable((By. XPATH, "//img[@src='/assets/selenium-logo-c1d6f4654a0c8f8bef745f71b4e22836224aabc2116f405ef511cd79c48f2947.png']")))
        # path pentru elementul unde se va muta fisierul sursa
        drag_to = WebDriverWait(self.chrome, 5).until(EC.element_to_be_clickable((By. ID, 'box')))
        # actiunea de drag and drop ce se executa
        ActionChains(self.chrome).drag_and_drop(drag_from,drag_to).perform()

        text_titlu = self.chrome.find_element(*self.TEXT_TITLU_PATH).text
        expected_text_titlu = "Drag the image into the box"
        assert text_titlu == expected_text_titlu, f"ERROR: Expected: {expected_text_titlu}, ACTUAL: {text_titlu}"
