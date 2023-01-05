
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Introducing_questions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Risk_appetite = models.StringField(choices=[['0', '0 (not at all willing)'], ['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8'], ['9', '9'], ['10', '10 (very willing)']], label='Are you generally a person who is willing to take risks or do you try to avoid taking risks? (Please tick a box on the scale, the value 0 means not at all willing to take risks and the value 10 means very willing to take risks)', widget=widgets.RadioSelectHorizontal)
    Current_investments = models.StringField(choices=[['Yes', 'Yes'], ['Not currently, but I used to invest', 'Not currently, but I used to invest'], ['No', 'No']], label='Do you currently invest money in stocks, bonds, mutual funds, or other financial instruments? ', widget=widgets.RadioSelect)
    Investment_experience = models.StringField(choices=[['1 (low)', '1 (low)'], ['2', '2'], ['3', '3'], ['4', '4'], ['5 (high)', '5 (high)']], label='How do you rate your investment experience?', widget=widgets.RadioSelectHorizontal)
    Statistical_knowledge = models.StringField(choices=[['1 (low)', '1 (low)'], ['2', '2'], ['3', '3'], ['4', '4'], ['5 (high)', '5 (high)']], label='How do you rate your statistical knowledge? ', widget=widgets.RadioSelectHorizontal)
class MyPage(Page):
    form_model = 'player'
    form_fields = ['Risk_appetite', 'Current_investments', 'Investment_experience', 'Statistical_knowledge']
page_sequence = [MyPage]