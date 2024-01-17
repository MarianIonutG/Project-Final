import time
from datetime import date
import unittest
# from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Introducere_Date(unittest.TestCase):
    ADDRESS = (By.ID, "autocomplete")
    STREET_NUMBER = (By.ID, "street_number")
    CITY = (By.ID, "locality")
    ADDRESS_NOT_FOUND_POP_UP = (By.XPATH,'// *[contains( @class ,"dismissButton")]')
    STATE = (By.ID, 'administrative_area_level_1')
    ZIP_CODE = (By.ID, 'postal_code')
    COUNTRY = (By.ID,'country')
    COMPONENTE = (By.ID,'navbarDropdownMenuLink')
    LINK_BUTTONS = (By.XPATH,'// *[contains( @class ,"dropdown-item")][2]')
    PRIMARY_BUTTON = (By.XPATH,'// *[contains( @class ,"btn btn-lg btn-primary")]')
    RIGHT_BUTTON = (By.XPATH,'// *[contains( @class ,"btn btn-lg btn-primary")][3]')
    MIDDLE_BUTTON = (By.XPATH, '// *[contains( @class ,"btn btn-lg btn-primary")][2]')
    DROPDOWN_BUTTON = (By.XPATH,'// *[contains( @class ,"btn btn-lg btn-primary dropdown-toggle")]')
    DROPDOWN_BUTTON_LINK_1 = (By.XPATH,'//*[text()="Dropdown link 1"]')
    DATEPICKER = (By.XPATH,'//*[text()="Datepicker"][1]')
    CELULA_DATEPICKER = (By.ID, 'datepicker')
    DATE_21_JANUARY = (By.XPATH, '//*[text()="21"]')
    SWITCH_WINDOW = (By.XPATH,'//*[text()="Switch Window"][1]')
    ALERTA = (By.ID, 'alert-button')
    OPEN_NEW_TAB = (By. ID, 'new-tab-button')
    WELLCOME_TO_NEW_PAGE = (By.XPATH,'// *[contains( @class ,"display-3")]')
    MODAL = (By.XPATH,'// *[contains( @class ,"dropdown-item")][10]')
    TEXT_AFISAT_MODAL = (By. XPATH,'// *[contains( @class ,"modal-body")]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_autocomplete(self):
        self.chrome.find_element(*self.ADDRESS).send_keys("Strada Sf. Nicolae") # Introducerea Strazii
        #time.sleep(2)
        self.chrome.find_element(*self.ADDRESS_NOT_FOUND_POP_UP).click() # Inchidere pop up de negasire a adresei
        #time.sleep(1)
        self.chrome.find_element(*self.STREET_NUMBER).send_keys("Numarul 6") # Introducerea numarului strazii
        #time.sleep(1)
        self.chrome.find_element(*self.CITY).send_keys("Tg-Jiu") # Introducerea Orasului
        #time.sleep(1)
        self.chrome.find_element(*self.STATE).send_keys("Gorj") # Introducerea Judetului
        #time.sleep(1)
        self.chrome.find_element(*self.ZIP_CODE).send_keys("210112") # Introducerea Codului Postal
        #time.sleep(1)
        self.chrome.find_element(*self.COUNTRY).send_keys("Romania") # Introducerea Tarii
        #time.sleep(1)


    def test_butoane(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        #time.sleep(2)
        self.chrome.find_element(*self.LINK_BUTTONS).click()
        #time.sleep(2)
        self.chrome.find_element(*self.PRIMARY_BUTTON).click() # apasarea butonului PRIMARY
        #time.sleep(2)
        text_buton_primary = self.chrome.find_element(*self.PRIMARY_BUTTON).text
        expected_buton_primary = "Primary"
        assert text_buton_primary == expected_buton_primary, f"ERROR: Expected: {expected_buton_primary}, ACTUAL: {text_buton_primary}"
        #time.sleep(1)
        self.chrome.find_element(*self.RIGHT_BUTTON).click() # apasarea butonului RIGHT
        #time.sleep(2)
        text_buton_dreapta = self.chrome.find_element(*self.RIGHT_BUTTON).text
        expected_buton_dreapta = "Right"
        assert text_buton_dreapta == expected_buton_dreapta, f"ERROR: Expected: {expected_buton_dreapta}, ACTUAL: {text_buton_dreapta}"
        #time.sleep(1)
        self.chrome.find_element(*self.MIDDLE_BUTTON).click()  # apasarea butonului MIDDLE
        #time.sleep(2)
        text_buton_mijloc = self.chrome.find_element(*self.MIDDLE_BUTTON).text
        expected_buton_mijloc = "Middle"
        assert text_buton_mijloc == expected_buton_mijloc, f"ERROR: Expected: {expected_buton_mijloc}, ACTUAL: {text_buton_mijloc}"
        #time.sleep(1)
        self.chrome.find_element(*self.DROPDOWN_BUTTON).click()
        #time.sleep(2)
        self.chrome.find_element(*self.DROPDOWN_BUTTON_LINK_1).click()
        #time.sleep(2)


    def test_alegere_data(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        #time.sleep(2)
        self.chrome.find_element(*self.DATEPICKER).click()
        #time.sleep(2)
        self.chrome.find_element(*self.CELULA_DATEPICKER).click()
        #time.sleep(2)
        self.chrome.find_element(*self.DATE_21_JANUARY).click()
        #time.sleep(2)
        text_data = self.chrome.find_element(*self.DATEPICKER).text
        expected_data = "02/21/2024"
        assert text_data == expected_data, f"ERROR: Expected: {expected_data}, ACTUAL: {text_data}"
        #time.sleep(1)

    def test_alerta(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        #time.sleep(2)
        self.chrome.find_element(*self.SWITCH_WINDOW).click()
        #time.sleep(2)
        self.chrome.find_element(*self.ALERTA).click()
        #time.sleep(2)
        buton_alerta = self.chrome.switch_to.alert
        buton_alerta.accept()
        text_buton_alerta = self.chrome.find_element(*self.ALERTA).text
        expected_buton_alerta = "Open alert"
        assert text_buton_alerta == expected_buton_alerta, f"ERROR: Expected: {expected_buton_alerta}, ACTUAL: {text_buton_alerta}"
        #time.sleep(1)

    def test_new_window(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        #time.sleep(2)
        self.chrome.find_element(*self.SWITCH_WINDOW).click()
        #time.sleep(2)
        self.chrome.find_element(*self.OPEN_NEW_TAB).click()
        #time.sleep(2)
        text_noul_tab = self.chrome.find_element(*self.WELLCOME_TO_NEW_PAGE).text
        expected_text_nou_tab = "Welcome to Formy"
        assert text_noul_tab == expected_text_nou_tab, f"ERROR: Expected: {expected_text_nou_tab}, ACTUAL: {text_noul_tab}"
        #time.sleep(1)

"""
    def test_modal(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        time.sleep(2)
        self.chrome.find_element(*self.MODAL).click()
        time.sleep(2)
        buton_modal = self.chrome.switch_to.frame('Modal title')
        text_afisat_modal = self.chrome.find_element(*self.TEXT_AFISAT_MODAL).text
        expected_text_afisat_modal = "Some text here"
        assert text_afisat_modal == expected_text_afisat_modal, f"ERROR: Expected: {expected_text_afisat_modal}, ACTUAL: {text_afisat_modal}"
        time.sleep(1)
"""