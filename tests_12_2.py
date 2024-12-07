import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            current_finished = dict()
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    current_finished[participant.name] = participant.distance
            if current_finished:
                sorted_keys = sorted(current_finished, key=current_finished.get)
                # print(type(sorted_keys))
                sorted_keys.reverse()

                for name in sorted_keys:
                    runner = next(p for p in self.participants if p.name == name)
                    finishers[place] = runner
                    place += 1
                    self.participants.remove(runner)
                    # finishers[place] = participant
                    # place += 1
                    # self.participants.remove(participant)

        return finishers
    
class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()
        cls.is_frozen = True

    def setUp(self):
        self.usein = Runner('Усэйн', 10)
        self.andre = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tour_1 = Tournament(90, self.usein, self.nick)    
        TournamentTest.all_results['1'] = tour_1.start()

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tour_2 = Tournament(90, self.andre, self.nick)    
        TournamentTest.all_results['2'] = tour_2.start()

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tour_3 = Tournament(90, self.usein, self.andre, self.nick)    
        TournamentTest.all_results['3'] = tour_3.start()

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tournament_4(self):
        tour_4 = Tournament(9, self.andre, self.usein, self.nick)    
        TournamentTest.all_results['4'] = tour_4.start()

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            finishers = cls.all_results[key]
            result_dict = {place: runner.name for place, runner in finishers.items()}
            print(result_dict)

if __name__ == '__main__':
    unittest.main()            