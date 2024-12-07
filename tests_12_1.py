from runner import Runner
from unittest import TestCase
import unittest
class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test = Runner('name')
        for _ in range(10):
            test.walk()
        self.assertEqual(test.distance, 50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        test = Runner('name')
        for _ in range(10):
            test.run()
        self.assertEqual(test.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test = Runner('name')
        test1 = Runner('name1')
        for _ in range(10):
            test.run()
            test1.walk()
        self.assertNotEqual(test.distance, test1.distance)

if __name__ == '__main__':
    unittest.main()

