import importlib

game_options = ['guess', 'hangman']
selected_game = ''

while (not selected_game in game_options):
  print(f'Game options: {game_options}')
  selected_game = input('Select: ')

game_module = importlib.import_module(f'{selected_game}.game')

game = game_module.game_instance()
game.start()
