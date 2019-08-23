import random
import logbook

player_log = logbook.Logger('PLAYERS_LOG')

computer_names = ['Dozer', 'Petra Leuchter', 'A. Fast']


class Player:
    def __init__(self, name):
        self.name = name
        self.current_roll = None
        self.current_score = 0

    def pick_current_roll(self, rolls):
        while True:
            try:
                self.current_roll = rolls[(input('Pick your favourite weapon: Rock, Paper or Scissors? >>> ').lower())]
                break
            except KeyError:
                print()
                print('Unknown weapon picked. Please pick a valid weapon.')
                print()
                continue

    @staticmethod
    def get_players_name():
        player_name = input('Dear player! What is your name?: ')
        print()
        print(f'Hi {player_name}!')
        player_log.info(f'Player name: {player_name}')
        return player_name

    @staticmethod
    def get_computer_name():
        computer_name = random.choice(computer_names)
        print(f'Your opponent today is: {computer_name}')
        player_log.info(f'Computer name: {computer_name}')
        return computer_name



