import random
from result_handler import result_handler
from rolls import Roll
from players import Player
from print_output import print_header, print_round_count, print_choices, print_congratulations
import logbook
import sys

game_log = logbook.Logger('GAME_LOG')


def main():
    print_header()
    player1 = Player(Player.get_players_name())
    player2 = Player(Player.get_computer_name())
    rolls = Roll.build_the_three_rolls()
    game_loop(player1, player2, rolls)
    

def find_winner(player1, player2):
    if player1.current_score == 2:
        winner = player1.name
    if player2.current_score == 2:
        winner = player2.name
    return winner


def game_loop(player1, player2, rolls):
    game_log.info(f'Game started')
    count = 1
    player1.current_score = 0
    player2.current_score = 0
    while player1.current_score < 2 and player2.current_score < 2:
        print_round_count(count)
        game_log.info(f'Round {count}')

#       get rolls for current round
        player2.current_roll = random.choice(list(rolls.values()))
        player1.pick_current_roll(rolls)
        print_choices(player1, player2)
        game_log.info(f'Roll of {player1.name}: {player1.current_roll.name}')
        game_log.info(f'Roll of {player2.name}: {player2.current_roll.name}')

#       round results
        round_result = player1.current_roll.fight_against(player2.current_roll)
        result_handler.get(round_result)(player1, player2)
        game_log.info(f'{player1.name}: {round_result}')
        game_log.info(f'{player1.name}: {player1.current_score}')
        game_log.info(f'{player2.name}: {player2.current_score}')

        if round_result in ('win', 'lose'): count += 1

    winner = find_winner(player1, player2)
    print_congratulations(winner)
    game_log.info(f'Winner: {winner}')
    game_log.info(f'Game ended')


def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(level,
                                                            "stdout mode" if not filename else 'file mode: ' + filename
                                                            )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging(r'log/game.log')
    main()
