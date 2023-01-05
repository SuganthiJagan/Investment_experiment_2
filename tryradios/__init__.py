
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'tryradios'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    risk_appetite = models.StringField(choices=[['1a', '1aaaaaaaaaaaaa'], ['2v', '2v'], ['3c', '3c']], label='please answer question below', widget=widgets.RadioSelectHorizontal)
    test2 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3']], label='please answer also this quessiton below', widget=widgets.RadioSelect)
class MyPage(Page):
    form_model = 'player'
    form_fields = ['risk_appetite', 'test2']
page_sequence = [MyPage]