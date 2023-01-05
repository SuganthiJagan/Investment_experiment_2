
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Control_variables'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Gender = models.StringField(choices=[['female', 'Female'], ['male', 'Male'], ['Non-binary', 'Non-binary']], label='Gender')
    Occupation = models.StringField(choices=[['Accounting & Controlling', 'Accounting & Controlling'], ['Advisory Services', 'Advisory Services'], ['Analysis & Research', 'Analysis & Research'], ['Fund & PF Management', 'Fund & PF Management'], ['Administration', 'Administration'], ['Investment Banking', 'Investment Banking'], ['Private Banking', 'Private Banking'], ['Risk Management', 'Risk Management'], ['Sales', 'Sales'], ['Management', 'Management'], ['Trading, Brokerage', 'Trading, Brokerage'], ['Other: Finance', 'Other: Finance'], ['Other: Non-Finance', 'Other: Non-Finance']], label='Occupation')
    Education = models.StringField(choices=[['High school', 'High school'], ['Undergraduate degree', 'Undergraduate degree'], ['Graduate degree', 'Graduate degree'], ['MBA', 'MBA'], ['Ph.D.', 'Ph.D.']], label='Highest degree')
    Age = models.StringField(choices=[['18 - 29', '18 - 29'], ['30 - 39', '30 - 39'], ['40 - 49', '40 - 49'], ['50 - 59', '50 - 59'], ['60 - 69', '60 - 69'], ['70 - 79', '70 - 79'], ['80 - 89', '80 - 89'], ['90 - 99', '90 - 99']], label='Age')
def custom_export(players):
    yield ['participant_code', 'id_in_group']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group]
class MyPage(Page):
    form_model = 'player'
    form_fields = ['Age', 'Gender', 'Occupation', 'Education']
page_sequence = [MyPage]