import random
import sys

ballsleft = 90
balls = random.sample(range(1, 91), 90)

class Player:
    def __init__(self):
        self.number = 15
        self.name = name
        self.numbers_card = random.sample(range(1, 91), 15)
        self.numbers_line = [self.numbers_card[:5], self.numbers_card[5:10], self.numbers_card[10:]]
        for line in self.numbers_line:
            line.sort()
            line.insert(random.randint(0, 4), ' ')
            line.insert(random.randint(0, 5), ' ')
            line.insert(random.randint(0, 6), ' ')
            line.insert(random.randint(0, 7), ' ')

    def take_card(self):
        print('{:-^26}'.format(' Карточка'+ self.name))
        for line1 in self.numbers_line:
            for number1 in line1:
                print('{0:>2}'.format(number1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))

    def move(self):
        while True:
            a = input('Зачеркнуть цифру? (y/n): ')
            if a == 'y':
                if ball in self.numbers_card:
                    for l in self.numbers_line:
                        try:
                            l.insert(l.index(ball), '><')
                            l.pop(l.index(ball))
                        except ValueError:
                            continue
                    print('\nOK')
                    return 1
                    break
                else:
                    print('\nGAME OVER')
                    sys.exit()
            if a == 'n':
                if ball in self.numbers_card:
                    print('\nGAME OVER')
                    sys.exit()
                else:
                    print('\nOK')
                    break
            else:
                print("Используйте символ (y/n)")

class CompPlayer(Player):
    def move(self):
        if ball in self.numbers_card:
            for i in self.numbers_line:
                try:
                    i.insert(i.index(ball), '><')
                    i.pop(i.index(ball))
                except ValueError:
                    continue
            return 1

players_person = {}
player_card = None

while True:
    try:
        count_players = int(input("Введите количество игроков"))
        for i in range(count_players):
            type_player = input("Этот игрок компьтер/человек? (y/любой символ)")
            if type_player == "y":
                name = input("Введите рабочее название: ")
                if name in players_person:
                    print("Такой игрок уже есть!")
                else:
                    players_person[name] = CompPlayer()
            else:
                name = input("Введите имя игрока: ")
                if name in players_person:
                    print("Такой игрок уже есть!")
                else:
                    players_person[name] = Player()

        for ball in balls:
            ballsleft -= 1
            print('\nНовый бочонок: {} (осталось: {})\n'.format(ball, ballsleft))

            for name in players_person:
                player_card = players_person[name]
                player_card.take_card()

                if player_card.move() == 1:
                    player_card.number -= 1

                if player_card.number == 0:
                    print('\nУ нас победитель! Игрок ' + name)
                    sys.exit()
                if ballsleft == 0:
                    print('\nGAME OVER')
                    sys.exit()
    except ValueError:
        print("Количество игроков вводиться цифрами!")