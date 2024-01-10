import time
from datetime import date
import unittest
# from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Autentificare(unittest.TestCase):
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

	def setUp(self) -> None:
		self.chrome = webdriver.Chrome()
		self.chrome.maximize_window()
		self.chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
		self.chrome.implicitly_wait(6)

	def tearDown(self) -> None:
		self.chrome.quit()


	def test_fillData(self):
		today = "{:%B %d, %Y}".format(date.today())
		self.chrome.find_element(*self.ACCEPT_ONLY_NECESSARIES).click()
		time.sleep(5)
		self.chrome.find_element(*self.DISMISS_BUTTON).click()
		time.sleep(2)
		self.chrome.find_element(*self.FIRST_NAME).send_keys("Doru")
		time.sleep(1)
		self.chrome.find_element(*self.LAST_NAME).send_keys("Popescu")
		time.sleep(1)
		self.chrome.find_element(*self.GENDER_FEMININ).click()  # selectie Gender Feminin
		time.sleep(0.5)
		self.chrome.find_element(*self.GENDER_MASCULIN).click() # selectie Gender Masculin
		time.sleep(0.5)
		self.chrome.find_element(*self.EXPERIENTA_MUNCA[0]).click()  # selectie Experienta de munca de 1 an
		time.sleep(0.2)
		self.chrome.find_element(*self.EXPERIENTA_MUNCA[1]).click()  # selectie Experienta de munca de 2 an
		time.sleep(0.2)
		self.chrome.find_element(*self.EXPERIENTA_MUNCA[2]).click()  # selectie Experienta de munca de 3 an
		time.sleep(0.2)
		self.chrome.find_element(*self.EXPERIENTA_MUNCA[3]).click()  # selectie Experienta de munca de 4 an
		time.sleep(0.2)
		self.chrome.find_element(*self.EXPERIENTA_MUNCA[4]).click()  # selectie Experienta de munca de 5 an
		time.sleep(0.2)
		self.chrome.find_element(*self.EXPERIENTA_MUNCA[5]).click()  # selectie Experienta de munca de 6 an
		time.sleep(0.2)
		self.chrome.find_element(*self.EXPERIENTA_MUNCA[6]).click()  # selectie Experienta de munca de 7 an
		time.sleep(0.2)
		self.chrome.find_element(*self.CURRENT_DATE).send_keys(str(today)) # data curenta este adaugata
		time.sleep(3)
		self.chrome.find_element(By. XPATH,'//*[contains(@id,"profession-0")][1]').click() # casuta de manual tester poate fi checkuita
		time.sleep(3)
		self.chrome.find_element(By. XPATH,'//*[contains(@id,"profession-0")][1]').click()  # casuta de manual tester poate fi decheckuita
		time.sleep(3)
		self.chrome.find_element(By. XPATH,'//*[contains(@id,"profession-1")][1]').click() # casuta de automation tester poate fi checkuita
		time.sleep(3)
		self.chrome.find_element(By. XPATH,'//*[contains(@id,"profession-1")][1]').click() # casuta de automation tester poate fi decheckuita
		time.sleep(3)
		casuta_buton_tester_manual = self.chrome.find_element(By.XPATH, '//*[contains(@id,"profession-0")][1]')
		time.sleep(2)
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

	#if (self.chrome.find_element(*self.PROFESSION_MANUAL_TESTER).isSelected() != 1):
		#	self.chrome.find_element(*self.PROFESSION_MANUAL_TESTER).click()
		#	time.sleep(3)
"""
	def test_PROFESSION_Automat_Tester_Selected(self):
		self.chrome.find_element(*self.PROFESSION_AUTOMATION_TESTER).click()
		time.sleep(3)
		if(self.chrome.find_element(*self.PROFESSION_AUTOMATION_TESTER).isSelected() != 1):
			self.chrome.find_element(*self.PROFESSION_AUTOMATION_TESTER).click()
			time.sleep(3)


				js_alert_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
				
				
				
				
				
				
				
				
				
				
				
				  
				expected_text = 'You successfully clicked an alert'
				assert js_alert_text == expected_text,f"ERROR: Expected: {expected_text}, Actual: {js_alert_text}"


"""




