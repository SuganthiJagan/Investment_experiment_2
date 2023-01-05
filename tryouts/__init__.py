
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'tryouts'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    RANDOMISE_QUESTION_ORDER = True
    BASE_PAYMENT = cu(1)
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    age = models.IntegerField(label='age')
    name = models.StringField(label='name')
    aaa = models.IntegerField(label='aaa')
    bbb = models.IntegerField(label='bbb')
class MyPage(Page):
    form_model = 'player'
    form_fields = ['age', 'name', 'aaa', 'bbb']
    @staticmethod
    def get_form_fields(player: Player):
        import random
        form_fields = ['age', 'name', 'aaa', 'bbb']
        random.shuffle(form_fields)
        return form_fields
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(age=12)
        
        if values != solutions:
            return "One or more answers were incorrect."
class Results(Page):
    form_model = 'player'
page_sequence = [MyPage, Results]