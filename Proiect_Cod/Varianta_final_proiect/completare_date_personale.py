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

class completare_date_personale(unittest.TestCase):

    ADDRESS = (By.ID, "autocomplete")
    STREET_NUMBER = (By.ID, "street_number")
    CITY = (By.ID, "locality")
    ADDRESS_NOT_FOUND_POP_UP = (By.XPATH, '// *[contains( @class ,"dismissButton")]')
    STATE = (By.ID, 'administrative_area_level_1')
    ZIP_CODE = (By.ID, 'postal_code')
    COUNTRY = (By.ID, 'country')
    TITLU_FORMULAR = (By. XPATH, "//div[@class='container']/h1")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    #Introducerea datelor personale si verificarea titlului formularului
    def test_autocomplete(self):
        self.chrome.find_element(*self.ADDRESS).send_keys("Strada Sf. Nicolae") # Introducerea Strazii
        self.chrome.find_element(*self.ADDRESS_NOT_FOUND_POP_UP).click() # Inchidere pop up de negasire a adresei
        self.chrome.find_element(*self.STREET_NUMBER).send_keys("Numarul 6") # Introducerea numarului strazii
        self.chrome.find_element(*self.CITY).send_keys("Tg-Jiu") # Introducerea Orasului
        self.chrome.find_element(*self.STATE).send_keys("Gorj") # Introducerea Judetului
        self.chrome.find_element(*self.ZIP_CODE).send_keys("210112") # Introducerea Codului Postal
        self.chrome.find_element(*self.COUNTRY).send_keys("Romania") # Introducerea Tarii

        nume_formular = self.chrome.find_element(*self.TITLU_FORMULAR).text
        nume_formular_asteptat = 'Autocomplete'
        assert nume_formular == nume_formular_asteptat, f"ERROR: Expected: {nume_formular_asteptat}, ACTUAL: {nume_formular}"