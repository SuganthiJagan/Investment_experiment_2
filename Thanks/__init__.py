
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Thanks'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass
class MyPage(Page):
    form_model = 'player'
class Redirect(Page):
    form_model = 'player'
    @staticmethod
    def js_vars(player: Player):
        return dict(redirect_url='https://www.cloudresearch.com/')
page_sequence = [MyPage, Redirect]