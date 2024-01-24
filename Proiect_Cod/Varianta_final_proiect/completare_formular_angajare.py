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

class completare_formular_angajare(unittest.TestCase):

    COMPONENTE = (By.ID,'navbarDropdownMenuLink')
    COMPLETE_FORM = (By.XPATH,'//*[text()="Complete Web Form"][1]')
    prenume_formular = (By.ID, 'first-name')
    nume_formular = (By.ID, 'last-name')
    meserie_formular = (By.ID, 'job-title')
    nivel_educatie_colegiu_formular = (By.ID, 'radio-button-2')
    sex_formular = (By.ID, 'checkbox-1')
    ani_experienta_de_ales_formular = (By.ID, 'select-menu')
    ani_experienta_doi_patru_ani = (By.XPATH, '//*[text()="2-4"]')
    DATA_FORMULAR = (By.ID, 'datepicker')
    DATA_SASE_IANUARIE = (By.XPATH, '// *[contains( @ data-date, "1704499200000")]') # corespunde datei de 06.01.2024
    SUBMIT_BUTTON_FORMULAR = (By.XPATH, '// *[contains( @class ,"btn btn-lg btn-primary")]')
    CONFIRMARE_FORMULAR = (By.XPATH, '// *[contains( @class ,"alert alert-success")]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    # Functie de autentificare cu nume introdus
    def test_complete_web_form_nume_inserat(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.COMPLETE_FORM).click()
        self.chrome.find_element(*self.prenume_formular).send_keys('Dan')
        self.chrome.find_element(*self.nume_formular).send_keys('Maftei')
        self.chrome.find_element(*self.meserie_formular).send_keys('Mecanic')
        self.chrome.find_element(*self.nivel_educatie_colegiu_formular).click()
        self.chrome.find_element(*self.sex_formular).click()
        self.chrome.find_element(*self.ani_experienta_de_ales_formular).click()
        self.chrome.find_element(*self.ani_experienta_doi_patru_ani).click()
        self.chrome.find_element(*self.DATA_FORMULAR).click()
        data_aleasa = self.chrome.find_element(*self.DATA_SASE_IANUARIE)
        data_aleasa.click()
        self.chrome.find_element(*self.SUBMIT_BUTTON_FORMULAR).click()

        text_confirmare_formular = self.chrome.find_element(*self.CONFIRMARE_FORMULAR).text
        text_confirmare_asteptat_formular = 'The form was successfully submitted!'
        assert text_confirmare_formular == text_confirmare_asteptat_formular,f"ERROR: Expected: {text_confirmare_asteptat_formular}, ACTUAL: {text_confirmare_formular}"

    # Functie de autentificare fara nume introdus
    def test_complete_web_form_fara_nume_inserat(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.COMPLETE_FORM).click()
        self.chrome.find_element(*self.prenume_formular).send_keys('Dan')
        self.chrome.find_element(*self.meserie_formular).send_keys('Mecanic')
        self.chrome.find_element(*self.nivel_educatie_colegiu_formular).click()
        self.chrome.find_element(*self.sex_formular).click()
        self.chrome.find_element(*self.ani_experienta_de_ales_formular).click()
        self.chrome.find_element(*self.ani_experienta_doi_patru_ani).click()
        self.chrome.find_element(*self.DATA_FORMULAR).click()
        data_aleasa = self.chrome.find_element(*self.DATA_SASE_IANUARIE)
        data_aleasa.click()
        self.chrome.find_element(*self.SUBMIT_BUTTON_FORMULAR).click()

        text_confirmare_formular = self.chrome.find_element(*self.CONFIRMARE_FORMULAR).text
        text_confirmare_asteptat_formular = 'Please complete the name!'
        assert text_confirmare_formular == text_confirmare_asteptat_formular, f"ERROR: Expected: {text_confirmare_asteptat_formular}, ACTUAL: {text_confirmare_formular}"


    # Functie de autentificare fara nicio data introdusa
    def test_complete_web_form_date_inserate(self):
        self.chrome.find_element(*self.COMPONENTE).click()
        self.chrome.find_element(*self.COMPLETE_FORM).click()
        self.chrome.find_element(*self.SUBMIT_BUTTON_FORMULAR).click()

        text_confirmare_formular = self.chrome.find_element(*self.CONFIRMARE_FORMULAR).text
        text_confirmare_asteptat_formular = 'Please fill the form!'
        assert text_confirmare_formular == text_confirmare_asteptat_formular, f"ERROR: Expected: {text_confirmare_asteptat_formular}, ACTUAL: {text_confirmare_formular}"


