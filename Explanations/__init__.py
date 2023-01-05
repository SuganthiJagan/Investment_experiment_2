
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Explanations'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Explanation = models.StringField(choices=[['0,5 %', '0,5 %'], ['2 %', '2 %'], ['4%', '4%'], ['6 %', '6 %'], ['8 %', '8 %']], label='Please specify the resulting volatility. ')
    Payoffs = models.StringField(choices=[['4%', '4%'], ['6%', '6%'], ['8%', '8%'], ['10%', '10%'], ['12%', '12%'], ['14%', '14%']], label='Please select a a payoff structure.', widget=widgets.RadioSelectHorizontal)
class Explanations(Page):
    form_model = 'player'
    form_fields = ['Explanation']
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(Explanation="8 %")
        
        if values != solutions:
            return "Unfortunately, the selected answer is incorrect. Please take a look at the examples again and make sure that you understand the concept of leverage. Thank you!"
page_sequence = [Explanations]