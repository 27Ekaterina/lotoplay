import sys
from classes import Bag, Player, CompPlayer, Card, create_player

players_person = []
player_card = None
bag = Bag()
balls = bag.balls

while True:
    try:
        count_players = int(input("Введите количество игроков "))
        for i in range(count_players):
            type_player = input("Этот игрок компьтер/человек? (y/n) ")
            name = input("Введите имя: ")
            card = Card(name)
            player = create_player(name, type_player, card)
            players_person.append(player)

        for ball in balls:
            bag.ballsleft -= 1
            print('\nНовый бочонок: {},'.format(ball), bag)


            for name in players_person:
                print('{:-^26}'.format(' Карточка ' + name.card.name))
                name.card.take_card()
                print('{:-^26}\n'.format('-'))
                name.move(ball) == 1
                if bag.ballsleft == 0:
                    print('\nGAME OVER')
                    sys.exit()
    except ValueError:
        print("Количество игроков вводиться цифрами!")