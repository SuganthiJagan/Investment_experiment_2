
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'tryrandom'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
    MY_CONSTANT = 0
    TASKS = "'A', 'B', 'C','D','E','F','G','H','I"
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass
def my_function(player: Player):
    session = player.session
    subsession = player.subsession
    participant = player.participant
    import random
    
    if subsession.round_number == 1:
            for p in subsession.get_players():
                round_numbers = list(range(1, C.NUM_ROUNDS + 1))
                random.shuffle(round_numbers)
                task_rounds = dict(zip(C.TASKS, round_numbers))
                # print('player', p.id_in_subsession)
                # print('task_rounds is', task_rounds)
                p.participant.task_rounds = task_rounds
def custom_export(players):
    yield ['participant_code', 'id_in_group']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group]
class TaskA(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)
        
        participant = player.participant
        return player.round_number == participant.task_rounds['A']
class TaskB(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)
        
        participant = player.participant
        return player.round_number == participant.task_rounds['B']
class TaskC(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)
        
        participant = player.participant
        return player.round_number == participant.task_rounds['C']


class TaskD(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)

        participant = player.participant
        return player.round_number == participant.task_rounds['D']


class TaskE(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)

        participant = player.participant
        return player.round_number == participant.task_rounds['E']


class TaskF(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)

        participant = player.participant
        return player.round_number == participant.task_rounds['F']

class TaskG(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)

        participant = player.participant
        return player.round_number == participant.task_rounds['G']

class TaskH(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)

        participant = player.participant
        return player.round_number == participant.task_rounds['H']

class TaskI(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        my_function(player)

        participant = player.participant
        return player.round_number == participant.task_rounds['I']
page_sequence = [TaskA, TaskB, TaskC,TaskD, TaskE, TaskF,TaskG, TaskH, TaskI]