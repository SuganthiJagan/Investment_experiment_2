
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'tryrandom3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    question_displayed_this_round = models.IntegerField()
    Question1 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Question2 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Question3 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Question4 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Question5 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Question6 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Question7 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Question8 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')
    Question9 = models.StringField(
        choices=[['1:1', '1:1'], ['2:1', '2:1'], ['3:1', '3:1'], ['4:1', '4:1'], ['5:1', '5:1'], ['6:1', '6:1'],
                 ['7:1', '7:1'], ['8:1', '8:1'], ['9:1', '9:1'], ['10:1', '10:1']],
        label='Please specify the leverage you would apply on this stock. ')


global first_run, session_id
first_run = True
session_id = None
def my_function(player: Player):
    session = player.session
    global first_run, session_id
    print("----------------------------------")
    print("fr"+str(first_run))
    if first_run:
        session_id = session.id
    if session_id != session.id:
        first_run = True
        session_id = session.id
    print("glo sid"+str(session_id))
    print("otree sid"+str(session.id))
    print("fr"+str(first_run))
    subsession = player.subsession
    import random
    print("srn---"+str(subsession.round_number))
    if subsession.round_number == 1 and first_run:
        first_run = False
        list_of_question_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for player in subsession.get_players():
            temp_list = list_of_question_ids.copy()
            random.shuffle(temp_list)
            print(temp_list)
            player.in_round(1).question_displayed_this_round = temp_list.pop(0)
            player.in_round(2).question_displayed_this_round = temp_list.pop(0)
            player.in_round(3).question_displayed_this_round = temp_list.pop(0)
            player.in_round(4).question_displayed_this_round = temp_list.pop(0)
            player.in_round(5).question_displayed_this_round = temp_list.pop(0)
            player.in_round(6).question_displayed_this_round = temp_list.pop(0)
            player.in_round(7).question_displayed_this_round = temp_list.pop(0)
            player.in_round(8).question_displayed_this_round = temp_list.pop(0)
            player.in_round(9).question_displayed_this_round = temp_list.pop(0)



def custom_export(players):
    yield ['participant_code', 'id_in_group']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group]

class Question1(Page):
    form_model = 'player'
    form_fields = ['Question1']
    # player = Player()
    # my_function(player)
    # def is_displayed(self):
    #      my_function(self.player)
    #      return self.player.question_displayed_this_round == 1
    @staticmethod
    def is_displayed(player: Player):
        my_function(player)

        return player.question_displayed_this_round == 1

class Question2(Page):
    form_model = 'player'
    form_fields = ['Question2']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)

        return player.question_displayed_this_round == 2


class Question3(Page):
    form_model = 'player'
    form_fields = ['Question3']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)

        return player.question_displayed_this_round == 3


class Question4(Page):
    form_model = 'player'
    form_fields = ['Question4']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)

        return player.question_displayed_this_round == 4


class Question5(Page):
    form_model = 'player'
    form_fields = ['Question5']

    @staticmethod

    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 5


class Question6(Page):
    form_model = 'player'
    form_fields = ['Question6']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 6


class Question7(Page):
    form_model = 'player'
    form_fields = ['Question7']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 7


class Question8(Page):
    form_model = 'player'
    form_fields = ['Question8']

    @staticmethod
    def is_displayed(player: Player):
        my_function(player)
        return player.question_displayed_this_round == 8


class Question9(Page):
   form_model = 'player'
   form_fields = ['Question9']

   @staticmethod
   def is_displayed(player: Player):
       my_function(player)

       return player.question_displayed_this_round == 9



@staticmethod
def before_next_page(player: Player, timeout_happened):
    participant = player.participant
    participant.in_all_rounds = player.in_all_rounds()
    return participant
# def before_next_page(Page):
#     if player.in_round == 9:
#         print("Hello")
#         print(player.in_all_rounds)
#         player.participant.fields['player_in_all_rounds'] = player.in_all_rounds()

class Results(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.in_all_rounds
    # @staticmethod
    # def before_next_page(player: Player):
    #     player.participant.fields['player_in_all_rounds'] = player.in_all_rounds()


page_sequence = [Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9, Results]