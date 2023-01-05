
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Comprehension'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Backtesting = models.StringField(choices=[['0,6 %', '0,6 %'], ['1,7 %', '1,7 %'], ['3 %', '3 %'], ['8 %', '8 %'], ['15 %', '15 %']], label='Please specify the resulting volatility.')
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
class Backtesting(Page):
    form_model = 'player'
    form_fields = ['Backtesting']
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(Backtesting = "15 %")
        
        # error_message can return a dict whose keys are field names and whose
        # values are error messages
        errors = {f: 'Wrong' for f in solutions if values[f] != solutions[f]}
        # print('errors is', errors)
        if errors:
            player.num_failed_attempts += 1
            if player.num_failed_attempts >= 1:
                player.failed_too_many = True
                # we don't return any error here; just let the user proceed to the
                # next page, but the next page is the 'failed' page that boots them
                # from the experiment.
            else:
                return errors
class Failed(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many
page_sequence = [Backtesting, Failed]