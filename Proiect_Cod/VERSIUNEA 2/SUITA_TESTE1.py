import unittest
from Proiect_Cod.Autentificare import Autentificare
from Proiect_Cod.herokuapp import herokuapp

import HtmlTestRunner


class TestSuite(unittest.TestCase):

	def test_suite(self):
		test_de_rulat = unittest.TestSuite()
		test_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Autentificare),
								unittest.defaultTestLoader.loadTestsFromTestCase(herokuapp)])


		runner = HtmlTestRunner.HTMLTestRunner(
			combine_reports=True,
			report_title="Test Execution Report",
			report_name="Test Results"
		)

		runner.run(test_de_rulat)