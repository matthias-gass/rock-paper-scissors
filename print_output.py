def print_header():
    print('___________________________________')
    print('___________________________________')
    print()
    print('       Rock, Paper, Scissors')
    print('___________________________________')
    print('___________________________________')


def print_round_count(count):
    print()
    print('__________')
    print()
    print(f'Round {count}:')
    print('__________')
    print()


def print_choices(player1, player2):
    print()
    print(f'Choice of {player1.name}: {player1.current_roll.name}')
    print(f'Choice of {player2.name}: {player2.current_roll.name}')
    print()


def print_congratulations(winner):
    print()
    print(f'{winner} has won the game. Well done!')
