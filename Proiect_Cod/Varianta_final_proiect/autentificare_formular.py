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


class autentificare_formular(unittest.TestCase):
    ACCEPT_ONLY_NECESSARIES = (By.XPATH,'//*[contains(@id,"ez-accept-necessary")][1]')
    DISMISS_BUTTON = (By.XPATH,'//*[contains(@id,"cookieChoiceDismiss")]')
    FIRST_NAME = (By.NAME,"firstname")
    LAST_NAME = (By.NAME,"lastname")
    GENDER_MASCULIN = (By.ID, "sex-0")
    GENDER_FEMININ = (By.ID, "sex-1")
    EXPERIENTA_MUNCA = [(By.ID,"exp-0"),(By.ID,"exp-1"),(By.ID,"exp-2"),(By.ID,"exp-3"),(By.ID,"exp-4"),(By.ID,"exp-5"), (By.ID,"exp-6")]
    CURRENT_DATE = (By. ID,"datepicker")
    PROFESSION_MANUAL_TESTER = (By. XPATH,'//*[contains(@id,"profession-0")][1]')
    PROFESSION_AUTOMATION_TESTER = (By. XPATH,'//*[contains(@id,"profession-1")][1]')
    selectie_continent = (By.ID, 'continents')
    continent_ales = (By.XPATH,'//*[text()="Europe"]')
    share_button = (By. XPATH,'//*[contains(@class,"svg-icon-24")]')
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    # Completare formular si verificare continent ales coincide cu Europa
    def test_fillData(self):
        today = "{:%B %d, %Y}".format(date.today())
        self.chrome.find_element(*self.ACCEPT_ONLY_NECESSARIES).click()
        self.chrome.find_element(*self.DISMISS_BUTTON).click()
        self.chrome.find_element(*self.FIRST_NAME).send_keys("Doru")
        self.chrome.find_element(*self.LAST_NAME).send_keys("Popescu")
        self.chrome.find_element(*self.GENDER_FEMININ).click()  # selectie Gender Feminin
        self.chrome.find_element(*self.GENDER_MASCULIN).click() # selectie Gender Masculin
        self.chrome.find_element(*self.EXPERIENTA_MUNCA[0]).click()  # selectie Experienta de munca de 1 an
        self.chrome.find_element(*self.EXPERIENTA_MUNCA[1]).click()  # selectie Experienta de munca de 2 an
        self.chrome.find_element(*self.EXPERIENTA_MUNCA[2]).click()  # selectie Experienta de munca de 3 an
        self.chrome.find_element(*self.EXPERIENTA_MUNCA[3]).click()  # selectie Experienta de munca de 4 an
        self.chrome.find_element(*self.EXPERIENTA_MUNCA[4]).click()  # selectie Experienta de munca de 5 an
        self.chrome.find_element(*self.EXPERIENTA_MUNCA[5]).click()  # selectie Experienta de munca de 6 an
        self.chrome.find_element(*self.EXPERIENTA_MUNCA[6]).click()  # selectie Experienta de munca de 7 an
        self.chrome.find_element(*self.CURRENT_DATE).send_keys(str(today)) # data curenta este adaugata
        self.chrome.find_element(By. XPATH,'//*[contains(@id,"profession-0")][1]').click() # casuta de manual tester poate fi checkuita
        self.chrome.find_element(By. XPATH,'//*[contains(@id,"profession-0")][1]').click()  # casuta de manual tester poate fi decheckuita
        self.chrome.find_element(By. XPATH,'//*[contains(@id,"profession-1")][1]').click() # casuta de automation tester poate fi checkuita
        self.chrome.find_element(By. XPATH,'//*[contains(@id,"profession-1")][1]').click() # casuta de automation tester poate fi decheckuita
        casuta_buton_tester_manual = self.chrome.find_element(By.XPATH, '//*[contains(@id,"profession-0")][1]')

        if (casuta_buton_tester_manual.is_selected()):                                                        # verificam daca profesia de Tester manual este check uita
            print('The profession Manual tester is selected')
        else:
            print('The profession Manual tester is not selected')

        self.chrome.find_element(By.XPATH, '//*[contains(@id,"profession-1")][1]').click()
        casuta_buton_tester_automat = self.chrome.find_element(By.XPATH, '//*[contains(@id,"profession-1")][1]')
        time.sleep(2)
        if (casuta_buton_tester_automat.is_selected()):
            print('The profession Automation tester is selected')
        else:
            print('The profession Automation tester is not selected')

        self.chrome.find_element(*self.selectie_continent).click()
        time.sleep(1)
        self.chrome.find_element(*self.continent_ales).click()
        text_continent_ales = self.chrome.find_element(*self.continent_ales).text
        expected_text = "Europe"
        assert text_continent_ales == expected_text, f"ERROR: Expected: {expected_text}, ACTUAL: {text_continent_ales}"

    # Verificare optiune Selenium Commands corespunde cu optiunea aleasa, in cazul asta Switch Commands
    def test_dropdown(self):
        dropdown_web = self.chrome.find_element(By.ID, 'selenium_commands')
        dropdown_web.find_element(By.XPATH, "//option[. = 'Switch Commands']").click()
        text_comanda_aleasa = dropdown_web.find_element(By.XPATH, "//option[. = 'Switch Commands']").text
        expected_text_comanda_aleasa = "Switch Commands"
        assert text_comanda_aleasa == expected_text_comanda_aleasa, f"ERROR: Expected: {expected_text_comanda_aleasa}, ACTUAL: {text_comanda_aleasa}"
        time.sleep(1)
