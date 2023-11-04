import unittest
from statistics_service import StatisticsService
from player import Player

from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_works(self):
        self.assertEqual('Semenko', self.stats.search('Semenko').name)
        self.assertIsNone(self.stats.search('Jalmari'))

    def test_team_method_works(self):
        players = self.stats.team("PIT")
        self.assertEqual(1, len(players))
        self.assertEqual('Lemieux', players[0].name)

    def test_top_method_works(self):
        top_players = self.stats.top(3)
        self.assertEqual(3, len(top_players))

    def test_top_method_works_goals(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual('Lemieux', top_players[0].name)
        self.assertEqual("Yzerman", top_players[1].name)

    def test_top_method_works_assists(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual('Gretzky', top_players[0].name)
        self.assertEqual("Yzerman", top_players[1].name)

    def test_top_method_works_points(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual('Gretzky', top_players[0].name)
        self.assertEqual("Lemieux", top_players[1].name)
