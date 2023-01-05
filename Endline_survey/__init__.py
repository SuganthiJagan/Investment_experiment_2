
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Endline_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Understanding = models.StringField(choices=[['Strongly agree', 'Strongly agree'], ['Agree', 'Agree'], ['Neutral', 'Neutral'], ['Disagree', 'Disagree'], ['Strongly disagree', 'Strongly disagree']], label='I did understand the questions in this study well. ', widget=widgets.RadioSelect)
    Agenda1 = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Do you think the researchers in this study had an agenda?')
    Agenda2 = models.LongStringField(blank=True, label='If yes, please state what do you think the research agenda was?')
class MyPage(Page):
    form_model = 'player'
    form_fields = ['Understanding', 'Agenda1', 'Agenda2']
page_sequence = [MyPage]