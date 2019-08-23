def draw(player1, player2):
    print(f'>>>>> It\'s a draw! Try again')


def win(player1, player2):
    player1.current_score += 1
    print(f'>>>>> Congratulations! You won!')
    print()
    print_score(player1, player2)


def lose(player1, player2):
    player2.current_score += 1
    print(f'>>>>> What a shame! You lost!')
    print_score(player1, player2)


def print_score(player1, player2):
    print()
    print(f'Score Player 1: {player1.current_score}')
    print(f'Score Player 2: {player2.current_score}')


result_handler = {'draw': draw,
                  'win': win,
                  'lose': lose
                  }
