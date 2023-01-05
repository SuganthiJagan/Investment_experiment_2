from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
#SESSION_CONFIGS = [dict(name='Leverage_choice', num_demo_participants=None, app_sequence=['trypayouts', 'Intro', 'Control_variables', 'Introducing_questions', 'Explanations', 'Comprehension', 'Treatments_intro', 'Treatments', 'Endline_survey', 'Thanks'])]
SESSION_CONFIGS = [dict(name='Leverage_choice', num_demo_participants=None, app_sequence=['Intro', 'Control_variables', 'Introducing_questions', 'Explanations', 'Comprehension', 'Treatments_intro','tryrandom4','Endline_survey', 'Thanks'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['selected_round', 'leverage', 'payoff_value', 'random_investment_option', 'return_investment']
SESSION_FIELDS = ['import random']
ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


