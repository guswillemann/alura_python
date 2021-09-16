import random
from copy import deepcopy

from .utils import *


class game_instance:
  def __init__(self):
    self.score = 1000
    self.secret_number = 0
    self.guesses_total = 0
    self.players = 1
    self.players_tags = ['Player1']
    self.winner = 0

  def setup(self):
    self.create_secret()
    self.set_players()
    if self.players == 1: self.set_difficulty()

  def start(self, replay = False):
    if not replay == 'replay': display_welcome()
    self.setup()
    
    if self.players == 1: self.play_single()
    else: self.play_multi()

    self.end()

  def end(self):
    end_text = (
      f'Your score: {self.score}',
      f'!!!Winner: {self.players_tags[self.winner]}!!!'
    )[self.players > 1]
    
    print(end_text)

    replay = query_replay()
    if replay: self.start('replay')

  def play_single(self):
    guesses_total = self.guesses_total
    secret_number = self.secret_number

    for guesses_current in range(1, guesses_total + 1):
      display_avaible_guesses(guesses_current, guesses_total)
      guess = query_guess()
      
      is_right_guess = guess == secret_number
      is_higher_guess = guess > secret_number
      is_last_guess = guesses_current == guesses_total

      if is_right_guess:
        print('You won!!!')
        break
      
      if is_last_guess:
        print(f'You LOSE!!! The number was {secret_number}')
        break
      
      if is_higher_guess: self.wrong_guess('higher', guess)
      else: self.wrong_guess('lower', guess)

  def play_multi(self):
    display_multiplayer_instructions()
    
    players_list = deepcopy(self.players_tags)
    current_round = 1

    while len(players_list) > 1:
      new_players_list = []
      print(f'\nRound: {current_round}')
      for i in players_list:
        print(f"{i}'s turn")
        guess = query_guess(True)
        
        is_right_guess = guess == self.secret_number
        is_higher_guess = guess > self.secret_number

        if is_right_guess:
          print('Your guess is right!!!')
          new_players_list.append(i)

        elif is_higher_guess: self.wrong_guess('higher')
        else: self.wrong_guess('lower')

      if len(new_players_list) > 0:
        current_round = current_round + 1
        players_list = new_players_list
        self.create_secret()
    
  def create_secret(self):
    self.secret_number = random.randrange(1, 101)

  def set_difficulty(self):
    difficulty_level = query_difficulty()

    difficulty_level_avaible_guesses = {
      '1': 20,
      '2': 10,
      '3': 5
    }

    self.guesses_total = difficulty_level_avaible_guesses[difficulty_level]
  
  def set_players(self):
    self.players = query_player_quantity()
    if self.players > 1:
      self.players_tags = query_player_tags(self.players)

  def wrong_guess(self, message, guess = 0):
    if self.players == 1:
      self.score = self.score - abs(self.secret_number - guess)
    print(f'Wrong!!! Your guess is {message}')
