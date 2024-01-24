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

class administrare_butoane(unittest.TestCase):

    COMPONENTE = (By.ID, 'navbarDropdownMenuLink')
    LINK_BUTTONS = (By.XPATH, '// *[contains( @class ,"dropdown-item")][2]')
    PRIMARY_BUTTON = (By.XPATH, '// *[contains( @class ,"btn btn-lg btn-primary")]')
    RIGHT_BUTTON = (By.XPATH, '// *[contains( @class ,"btn btn-lg btn-primary")][3]')
    MIDDLE_BUTTON = (By.XPATH, '// *[contains( @class ,"btn btn-lg btn-primary")][2]')
    DROPDOWN_BUTTON = (By.XPATH, '// *[contains( @class ,"btn btn-lg btn-primary dropdown-toggle")]')
    DROPDOWN_BUTTON_LINK_1 = (By.XPATH, '//*[text()="Dropdown link 1"]')
    DROPDOWN_BUTTON_LINK_1_path = (By.XPATH,"//div[@class='dropdown-menu show']/a[1]")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    # Verificare apasare buton Primary
    def test_primary_button(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.LINK_BUTTONS).click()
        self.chrome.find_element(*self.PRIMARY_BUTTON).click()  # apasarea butonului PRIMARY

        text_buton_primary = self.chrome.find_element(*self.PRIMARY_BUTTON).text
        expected_buton_primary = "Primary"
        assert text_buton_primary == expected_buton_primary, f"ERROR: Expected: {expected_buton_primary}, ACTUAL: {text_buton_primary}"

    # Verificare apasare buton RIGHT
    def test_right_button(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.LINK_BUTTONS).click()
        self.chrome.find_element(*self.RIGHT_BUTTON).click()  # apasarea butonului RIGHT

        text_buton_dreapta = self.chrome.find_element(*self.RIGHT_BUTTON).text
        expected_buton_dreapta = "Right"
        assert text_buton_dreapta == expected_buton_dreapta, f"ERROR: Expected: {expected_buton_dreapta}, ACTUAL: {text_buton_dreapta}"

    # Verificare apasare buton MIDDLE
    def test_middle_button(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.LINK_BUTTONS).click()
        self.chrome.find_element(*self.MIDDLE_BUTTON).click()  # apasarea butonului MIDDLE

        text_buton_mijloc = self.chrome.find_element(*self.MIDDLE_BUTTON).text
        expected_buton_mijloc = "Middle"
        assert text_buton_mijloc == expected_buton_mijloc, f"ERROR: Expected: {expected_buton_mijloc}, ACTUAL: {text_buton_mijloc}"

    # Verificare apasare buton DROPDOWN si selectare DROPDOWN_LINK_1
    def test_dropdown_button(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.LINK_BUTTONS).click()
        self.chrome.find_element(*self.DROPDOWN_BUTTON).click()
        text_buton_dropdown_link_1 = self.chrome.find_element(*self.DROPDOWN_BUTTON_LINK_1_path).text
        self.chrome.find_element(*self.DROPDOWN_BUTTON_LINK_1).click()
        self.chrome.find_element(*self.DROPDOWN_BUTTON).click()

        expected_buton_dropdown_link_1 = "Dropdown link 1"
        assert text_buton_dropdown_link_1 == expected_buton_dropdown_link_1, f"ERROR: Expected: {expected_buton_dropdown_link_1}, ACTUAL: {text_buton_dropdown_link_1}"