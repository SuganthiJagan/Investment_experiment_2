"Modified by Suganthi Last-Modified on: 05-Jan-2023"
from otree.api import *
from random import randrange


c = cu

doc = ''
test = []


class C(BaseConstants):
    NAME_IN_URL = 'tryrandom2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
    RANDOM_INVESTMENT_OPTION = randrange(1, 10)

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


global question_displayed, is_leverage_set
question_displayed = 0
is_leverage_set = False

def creating_session(subsession: Subsession):
    import random
    if subsession.round_number == 1:
        list_of_question_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for player in subsession.get_players():
            temp_list = list_of_question_ids.copy()
            random.shuffle(temp_list)
            print("Temp list" + str(temp_list))
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
    print(pp)



class Question1(Page):
    form_model = 'player'
    form_fields = ['Question1']

    #
    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 1:
            print("q1 displaying")
            global question_displayed
            question_displayed += 1
            return True


class Question2(Page):
    form_model = 'player'
    form_fields = ['Question2']

    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 2:
            print("q2 displaying")
            global question_displayed
            question_displayed += 1
            return True


class Question3(Page):
    form_model = 'player'
    form_fields = ['Question3']

    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 3:
            print("q3 displaying")
            global question_displayed
            question_displayed += 1
            return True


class Question4(Page):
    form_model = 'player'
    form_fields = ['Question4']

    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 4:
            print("q4 displaying")
            global question_displayed
            question_displayed += 1
            return True


class Question5(Page):
    form_model = 'player'
    form_fields = ['Question5']
    is_shown = False

    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 5:
            print("q5 displaying")
            global question_displayed
            question_displayed += 1
            return True


class Question6(Page):
    form_model = 'player'
    form_fields = ['Question6']

    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 6:
            print("q6 displaying")
            global question_displayed
            question_displayed += 1
            return True


class Question7(Page):
    form_model = 'player'
    form_fields = ['Question7']

    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 7:
            print("q7 displaying")
            global question_displayed
            question_displayed += 1
            return True


class Question8(Page):
    form_model = 'player'
    form_fields = ['Question8']

    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 8:
            print("q8 displaying")
            global question_displayed
            question_displayed += 1
            return True


class Question9(Page):
    form_model = 'player'
    form_fields = ['Question9']

    @staticmethod
    def is_displayed(player: Player):
        if player.question_displayed_this_round == 9:
            print("q9 displaying")
            global question_displayed
            question_displayed += 1
            return True


# @staticmethod
# def before_next_page(player: Player ):
#     print(C.NUM_ROUNDS)
#     subsession = player.subsession
#     print("in bnp")
#     print(player.subsession)
#     if subsession.round_number == C.NUM_ROUNDS:
#         print(player.in_all_rounds)

# def before_next_page(Page):
#     if player.in_round == 9:
#         print("Hello")
#         print(player.in_all_rounds)
#         player.participant.fields['player_in_all_rounds'] = player.in_all_rounds()

class Results(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        global question_displayed, is_leverage_set
        participant=player.participant
        print(question_displayed)
        print(is_leverage_set)
        if question_displayed > ((C.NUM_ROUNDS-1)*3):
            if not is_leverage_set:
                print("Calculating Results")
                is_leverage_set = True
                question_no = "Question" + str(C.RANDOM_INVESTMENT_OPTION)
                leverage = None
                for round_no in range(1, 10):
                    if leverage is None:
                        print(f"Round Number {round_no} leverage - {player.in_round(round_no).field_maybe_none(question_no)} ")
                        leverage = player.in_round(round_no).field_maybe_none(question_no)
                print("Results")
                print(f"Randomly Chosen Question {question_no}")
                print(f"User Chosen Answer {leverage}")
                import csv


                chosen_observation = None
                with open('all_returns.csv', 'r') as file:
                    my_reader = csv.reader(file, delimiter=',')
                    random_distribution = randrange(1, 201)
                    random_observation = C.RANDOM_INVESTMENT_OPTION
                    print(f"random distribution {random_distribution}")
                    print(f"random observation {random_observation}")
                    for row in my_reader:
                        row_no = int(row[0]) if row[0].isdigit() else None
                        if row_no == random_distribution:
                            print(row)
                            chosen_observation = float(row[random_observation])
                            break

                print(chosen_observation)
                leverage_factor = leverage.split(':', 1)[0]
                print("Leverage factor:"+leverage_factor)
                payoff_calculated = 2*(1+(float(leverage_factor)*chosen_observation))
                payoff_final = str(payoff_calculated)
                print("Payoff Calculated:"+payoff_final)
                #Set participant values
                participant.payoff_value = payoff_final
                participant.leverage = leverage
                participant.random_investment_option = round(random_observation, 2)
                participant.return_investment = chosen_observation


            return True


    # @staticmethod
    # def before_next_page(player: Player):
    #     player.participant.fields['player_in_all_rounds'] = player.in_all_rounds()


# @staticmethod
# def before_next_page(player: Player, timeout_happened):
#     if C.NUM_ROUNDS==9:
#         print(player.in_all_rounds)
#     return player.in_all_rounds


# class Results(Page):
#     @staticmethod
#     def is_displayed(player: Player):
#         return player.in_all_rounds


page_sequence = [Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9,
                 Results]
