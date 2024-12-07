import unittest
import tests_12_1
import tests_12_2

TS = unittest.TestSuite()
TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TS)
