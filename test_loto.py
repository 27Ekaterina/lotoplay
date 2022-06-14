import pytest
import random
import pytest_cov
from classes import Player, CompPlayer, Bag, Card

class TestBag:

    def setup(self):
        self.balls = random.sample(range(1, 4), 3)

    def test_balls(self):
        assert len(self.balls) == 3
        assert self.balls[2] in range(1,4)
        assert sorted(self.balls) == [1, 2, 3]

    def test_take_ball(self):
        result = random.choice(self.balls)
        assert result in self.balls
        assert result == 1 or 2 or 3

class TestCard:

    def setup(self, kate):
        self.card = Card(kate)

    def test_init(self):
        assert len(self.card.numbers_card) == 15
        for i in self.card.numbers_card:
            assert i in range(1, 91)


    def test_cross_number_comp(self):
        assert "><" in str(self.card)
        assert "&" not in str(self.card)
        self.card.cross_number_comp(1)
        self.card.cross_number_comp(2)
        self.card.cross_number_comp(3)
        self.card.cross_number_comp(4)
        self.card.cross_number_comp(5)
        self.card.cross_number_comp(6)
        self.card.cross_number_comp(7)
        self.card.cross_number_comp(8)
        self.card.cross_number_comp(9)
        self.card.cross_number_comp(10)
        self.card.cross_number_comp(11)
        self.card.cross_number_comp(12)
        self.card.cross_number_comp(13)
        self.card.cross_number_comp(14)
        self.card.cross_number_comp(15)
        self.card.cross_number_comp(16)
        self.card.cross_number_comp(17)
        self.card.cross_number_comp(18)
        self.card.cross_number_comp(19)
        self.card.cross_number_comp(20)
        self.card.cross_number_comp(21)
        self.card.cross_number_comp(22)
        self.card.cross_number_comp(23)
        self.card.cross_number_comp(24)
        self.card.cross_number_comp(25)
        self.card.cross_number_comp(26)
        self.card.cross_number_comp(27)
        self.card.cross_number_comp(28)
        self.card.cross_number_comp(29)
        self.card.cross_number_comp(30)
        assert self.card.number < 15

    def test_cross_number(self):
        assert "><" in str(self.card)
        assert "&" not in str(self.card)

    def test_not_cross_number(self):
        ball = [i for i in self.card.numbers_card]
        ball_in_play = ball[0]
        result = self.card.cross_number(ball_in_play)
        assert result == True


class TestPlayer:

    def setup(self, kate):
        self.name = "kate"
        self.card = Card(kate)
        self.player = Player(self.name, self.card)


    def test_init(self):
        assert len(self.player.card.numbers_card) == 15

    def test_str(self):
        result = "kate"
        assert result == str(self.player.name)

class TestCompPlayer:

    def setup(self, comp):
        self.name = "comp"
        self.card = Card(comp)
        self.player = CompPlayer(self.name, self.card)

    def test_move(self):
        ball = [i for i in self.card.numbers_card]
        for ball_in_play in ball:
            self.card.number -= 1
            return "У нас победитель! "
        assert self.player.move(ball_in_play) == "У нас победитель! "




