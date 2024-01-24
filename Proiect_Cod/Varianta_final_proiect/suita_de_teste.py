import unittest
import HtmlTestRunner
from CURS.Proiect_Examen.Varianta_final_proiect.administrare_alerte import administrare_alerte
from CURS.Proiect_Examen.Varianta_final_proiect.administrare_butoane import administrare_butoane
from CURS.Proiect_Examen.Varianta_final_proiect.administrare_drag_and_drop import administrare_drag_and_drop
from CURS.Proiect_Examen.Varianta_final_proiect.administrare_fereastra_modala import administrare_fereastra_modala
from CURS.Proiect_Examen.Varianta_final_proiect.autentificare_formular import autentificare_formular
from CURS.Proiect_Examen.Varianta_final_proiect.autentificare_nume_parola import autentificare_nume_parola
from CURS.Proiect_Examen.Varianta_final_proiect.completare_date_personale import completare_date_personale
from CURS.Proiect_Examen.Varianta_final_proiect.completare_formular_angajare import completare_formular_angajare
from CURS.Proiect_Examen.Varianta_final_proiect.tratare_add_uri import tratare_add_uri


class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_de_rulat = unittest.TestSuite()
        test_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(administrare_alerte),
                                unittest.defaultTestLoader.loadTestsFromTestCase(administrare_butoane),
                                unittest.defaultTestLoader.loadTestsFromTestCase(administrare_drag_and_drop),
                                unittest.defaultTestLoader.loadTestsFromTestCase(administrare_fereastra_modala),
                                unittest.defaultTestLoader.loadTestsFromTestCase(autentificare_formular),
                                unittest.defaultTestLoader.loadTestsFromTestCase(autentificare_nume_parola),
                                unittest.defaultTestLoader.loadTestsFromTestCase(completare_date_personale),
                                unittest.defaultTestLoader.loadTestsFromTestCase(completare_formular_angajare),unittest.defaultTestLoader.loadTestsFromTestCase(tratare_add_uri)])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Sumarul_testelor_executate", report_name="Rezultat_Teste")
        runner.run(test_de_rulat)