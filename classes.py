import sys
import random


class Bag:

    def __init__(self):
        self.ballsleft = 90
        self.balls = random.sample(range(1, 91), 90)

    def take_ball(self):
        result = random.choice(self.balls)
        return result

class Card:
    def __init__(self, name):
        self.name = name
        self.number = 15
        self.numbers_card = random.sample(range(1, 91), 15)
        self.numbers_line = [self.numbers_card[:5], self.numbers_card[5:10], self.numbers_card[10:]]
        for line in self.numbers_line:
            line.sort()
            line.insert(random.randint(0, 4), ' ')
            line.insert(random.randint(0, 5), ' ')
            line.insert(random.randint(0, 6), ' ')
            line.insert(random.randint(0, 7), ' ')

    def __str__(self):
        return '><' if self.cross_number_comp else self.numbers_line

    def take_card(self):
        for line1 in self.numbers_line:
            for number1 in line1:
                print('{0:>2}'.format(number1), end=' ')
            print()


    def cross_number_comp(self, ball):
        if ball in self.numbers_card:
            self.number -= 1
            if self.number == 0:
                print("У нас победитель! Игрок " + self.name)
                sys.exit()
            for i in self.numbers_line:
                try:
                    i.insert(i.index(ball), '><')
                    i.pop(i.index(ball))
                except ValueError:
                    continue
            return 1


    def cross_number(self, ball):
        if ball in self.numbers_card:
            self.number -= 1
            if self.number == 0:
                print("У нас победитель! Игрок " + self.name)
                sys.exit()
            for l in self.numbers_line:
                try:
                    l.insert(l.index(ball), '><')
                    l.pop(l.index(ball))
                except ValueError:
                    continue
            print('\nOK')
            return 1
        else:
            print('\nGAME OVER')
            sys.exit()

    def not_cross_number(self, ball):
        if ball in self.numbers_card:
            print('\nGAME OVER')
            sys.exit()
        else:
            print('\nOK')

class Player:
    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.number = 15

    def __str__(self):
        return str(self.name)

    def move(self, ball):
        while True:
            a = input('Зачеркнуть цифру? (y/n): ')
            if a == 'y':
                self.card.cross_number(ball)
                break
            if a == 'n':
                self.card.not_cross_number(ball)
                break
            else:
                print("Используйте символ (y/n)")

class CompPlayer(Player):
    def move(self, ball):
        self.card.cross_number_comp(ball)
        if self.number == 0:
            print("У нас победитель! ")

def create_player(name, type_player, card):
    players = {
        'y': CompPlayer,
        'n': Player
    }
    player = players[type_player](name, card)
    return player
