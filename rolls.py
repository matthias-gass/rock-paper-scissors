import logbook

roll_log = logbook.Logger('ROLLS_LOG')

decider = dict(rock={'rock': 'draw', 'scissors': 'win', 'paper': 'lose'},
               paper={'rock': 'win', 'scissors': 'lose', 'paper': 'draw'},
               scissors={'rock': 'lose', 'scissors': 'draw', 'paper': 'win'}
               )


class Roll:
    def __init__(self, name):
        self.name = name

    def fight_against(self, opponent):
        return decider[self.name][opponent.name]

    @staticmethod
    def build_the_three_rolls():
        rolls = dict()
        rolls['rock'] = Roll('rock')
        rolls['paper'] = Roll('paper')
        rolls['scissors'] = Roll('scissors')
        roll_log.info('Rolls have been successfully created')
        return rolls
