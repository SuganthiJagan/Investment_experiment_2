from otree.api import *
import random

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'Treatments'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_displayed_this_round = models.IntegerField()
    Treatment1 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Treatment2 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Treatment3 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Treatment4 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Treatment5 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Treatment6 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Treatment7 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Treatment8 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Treatment9 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')


def my_function(player: Player):
    session = player.session
    subsession = player.subsession

    if subsession.round_number == 1:
        list_of_question_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
        # list_of_question_ids = [1, 2, 3, 4]
        for player in subsession.get_players():
            temp_list = list_of_question_ids.copy()
            random.shuffle(temp_list)
            player.in_round(1).question_displayed_this_round = temp_list.pop(0)
            player.in_round(2).question_displayed_this_round = temp_list.pop(0)
            player.in_round(3).question_displayed_this_round = temp_list.pop(0)
            player.in_round(4).question_displayed_this_round = temp_list.pop(0)
            player.in_round(5).question_displayed_this_round = temp_list.pop(0)
            player.in_round(6).question_displayed_this_round = temp_list.pop(0)
            player.in_round(7).question_displayed_this_round = temp_list.pop(0)
            player.in_round(8).question_displayed_this_round = temp_list.pop(0)
            player.in_round(9).question_displayed_this_round = temp_list.pop(0)
            player.in_round(10).question_displayed_this_round = temp_list.pop(0)


class Treatment1(Page):
    form_model = 'player'
    form_fields = ['Treatment1']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)

        return player.question_displayed_this_round == 1


class Treatment2(Page):
    form_model = 'player'
    form_fields = ['Treatment2']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)

        return player.question_displayed_this_round == 2


class Treatment3(Page):
    form_model = 'player'
    form_fields = ['Treatment3']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)

        return player.question_displayed_this_round == 3


class Treatment4(Page):
    form_model = 'player'
    form_fields = ['Treatment4']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)

        return player.question_displayed_this_round == 4


class Treatment5(Page):
    form_model = 'player'
    form_fields = ['Treatment5']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 5


class Treatment6(Page):
    form_model = 'player'
    form_fields = ['Treatment6']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 6


class Treatment7(Page):
    form_model = 'player'
    form_fields = ['Treatment7']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 7


class Treatment8(Page):
    form_model = 'player'
    form_fields = ['Treatment8']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 8


class Treatment9(Page):
    form_model = 'player'
    form_fields = ['Treatment9']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 9


page_sequence = [Treatment1, Treatment2, Treatment3, Treatment4, Treatment5, Treatment6, Treatment7, Treatment8,
                 Treatment9]
