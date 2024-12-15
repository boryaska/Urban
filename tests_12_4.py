import logging
import unittest
from rt_with_exceptions import Runner

class RunnerTest(unittest.TestCase):
    # is_frozen = False

    # @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test = Runner('name', speed = -10 )
            for _ in range(10):
                test.walk()
            self.assertEqual(test.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)    

    # @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test = Runner(442)
            for _ in range(10):
                test.run()
            self.assertEqual(test.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
                

    # @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test = Runner('name')
        test1 = Runner('name1')
        for _ in range(10):
            test.run()
            test1.walk()
        self.assertNotEqual(test.distance, test1.distance)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    unittest.main()
    