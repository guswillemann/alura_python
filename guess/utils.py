from getpass import getpass

from .error_messages import error_messages


def display_welcome():
  print('*************************************')
  print('Welcome to a guessing game in Python!')
  print('*************************************')

def display_multiplayer_instructions():
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  print('!!!Game inputs will be hidden!!!')
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  print('-When a player correctly guess a')
  print(' number, a new one will be drawn')

def query_difficulty():
  print('Choose the difficulty level')
  print('(1) Easy (2) Medium (3) Hard')
  difficulty_input_str = input('select: ')

  input_options = ['1', '2', '3']
  input_attempts = 0

  while (not difficulty_input_str in input_options):
    # message_type = 'calm' if input_tentatives < 5 else 'impatient' if input_tentatives < 15 else 'furious'

    message_type = (
      ('impatient', 'furious')[input_attempts > 15],
      'calm'
    )[input_attempts < 5]

    print(error_messages['difficulty'][message_type])
    difficulty_input_str = input('select: ')
    input_attempts = input_attempts + 1

  return difficulty_input_str

def display_avaible_guesses(guesses_current, guesses_total):
  print(f'Guess {guesses_current} of {guesses_total}')

def query_guess(is_multiplayer = False):
  input_func = getpass if is_multiplayer else input

  guess_input_str = input_func('Guess a number in the range of 1 to 100: ')

  try:
    guess = int(guess_input_str)
  except:
    print(error_messages['guess']['not_a_number'])
    guess = query_guess(is_multiplayer)

  if (guess < 1 or guess > 100):
    print(error_messages['guess']['out_of_range'])
    guess = query_guess(is_multiplayer)
  
  return guess

def query_replay():
  print()
  replay_input_str = input('Would you like to play again?\n(Y/n)').lower()
  print()

  if (
    replay_input_str == 'y' or
    replay_input_str == ''
  ):
    return True
  elif (not replay_input_str == 'n'):
    return query_replay()
  
  return False

def query_player_quantity(message = ''):
  if (message): print(message)
  quantity_input_str = input('How many players? ')

  try:
    quantity = int(quantity_input_str)
    if (quantity > 0): return quantity
    return query_player_quantity(error_messages['players'])
  except:
    return query_player_quantity(error_messages['players'])

def query_player_tags(quantity):
  tag_list = []
  
  for i in range(0, quantity):
    tag_input = input(f'Player{i+1}: ')
    tag_list.append(tag_input)

  return tag_list
