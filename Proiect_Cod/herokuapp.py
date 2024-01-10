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
    DROPDOWN_BUTTON = (By.XPATH,'// *[contains( @class ,"btn btn-lg btn-primary dropdown-toggle")]')
    DROPDOWN_BUTTON_LINK_1 = (By.XPATH,'//*[text()="Dropdown link 1"]')
    DATEPICKER = (By.XPATH,'//*[text()="Datepicker"][1]')
    CELULA_DATEPICKER = (By.ID, 'datepicker')
    DATE_21_JANUARY = (By.XPATH, '//*[text()="21"]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_autocomplete(self):
        self.chrome.find_element(*self.ADDRESS).send_keys("Strada Sf. Nicolae") # Introducerea Strazii
        time.sleep(2)
        self.chrome.find_element(*self.ADDRESS_NOT_FOUND_POP_UP).click() # Inchider pop up de negasire a adresei
        time.sleep(1)
        self.chrome.find_element(*self.STREET_NUMBER).send_keys("Numarul 6") # Introducerea numarului strazii
        time.sleep(1)
        self.chrome.find_element(*self.CITY).send_keys("Tg-Jiu") # Introducerea Orasului
        time.sleep(1)
        self.chrome.find_element(*self.STATE).send_keys("Gorj") # Introducerea Judetului
        time.sleep(1)
        self.chrome.find_element(*self.ZIP_CODE).send_keys("210112") # Introducerea Codului Postal
        time.sleep(1)
        self.chrome.find_element(*self.COUNTRY).send_keys("Romania") # Introducerea Tarii
        time.sleep(1)

    @unittest.skip
    def test_butoane(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        time.sleep(2)
        self.chrome.find_element(*self.LINK_BUTTONS).click()
        time.sleep(2)
        self.chrome.find_element(*self.PRIMARY_BUTTON).click() # apasarea butonului PRIMARY
        time.sleep(2)
        self.chrome.find_element(*self.RIGHT_BUTTON).click() # apasarea butonului RIGHT
        time.sleep(2)
        self.chrome.find_element(*self.DROPDOWN_BUTTON).click()
        time.sleep(2)
        self.chrome.find_element(*self.DROPDOWN_BUTTON_LINK_1).click()
        time.sleep(2)

    def test_alegere_data(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        time.sleep(2)
        self.chrome.find_element(*self.DATEPICKER).click()
        time.sleep(2)
        self.chrome.find_element(*self.CELULA_DATEPICKER).click()
        time.sleep(2)
        self.chrome.find_element(*self.DATE_21_JANUARY).click()
        time.sleep(2)




