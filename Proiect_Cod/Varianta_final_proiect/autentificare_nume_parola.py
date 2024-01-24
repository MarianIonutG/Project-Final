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

class autentificare_nume_parola(unittest.TestCase):
    NUME = 'admin'
    PAROLA = 'admin'
    NUME_GRESIT = 'Razvan'
    MESAJ_CONFIRMARE = (By.XPATH, "//*[@id = 'content']/div/p")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(6)

    def tearDown(self) -> None:
        self.chrome.quit()

    # test autentificare cu nume si parola corecte
    def test_autentificare_reusit(self):
        self.chrome.get('https://' + self.NUME + ':' + self.PAROLA + '@the-internet.herokuapp.com/basic_auth')
        expected_text = "Congratulations! You must have the proper credentials."
        actual_text = self.chrome.find_element(*self.MESAJ_CONFIRMARE).text
        assert expected_text == actual_text, f"ERROR: Expected: {expected_text}, ACTUAL: {actual_text}"

    @unittest.skip # Va sari peste rularea acestui test
    # autentificare cu nume gresit si parola corecta
    def test_autentificare_nume_gresit(self):
        self.chrome.get('https://' + self.NUME_GRESIT + ':' + self.PAROLA + '@the-internet.herokuapp.com/basic_auth')
        expected_text = "Congratulations! You must have the proper credentials."
        actual_text = self.chrome.find_element(*self.MESAJ_CONFIRMARE).text
        assert expected_text == actual_text, f"ERROR: Expected: {expected_text}, ACTUAL: {actual_text}"

