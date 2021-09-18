import random

class game_instance:
  def __init__(self):
    with open('hangman/words.txt', 'r') as words_file:
      self.words = [word.strip() for word in words_file]

    self.secret_word = ''
    self.right_letters = []
  
  def get_word(self): 
    total_words = len(self.words)
    return self.words[random.randrange(0, total_words)]

  def setup(self):
    self.secret_word = self.get_word().upper()
    self.right_letters = ['_' for letter in self.secret_word]

  def start(self, replay = False):
    if (not replay): display_welcome()
    self.setup()

    is_right_guess = False
    out_of_guesses = False
    wrong_guesses = 0
    total_guesses = 7

    self.display_word_letters()
    
    while (not out_of_guesses and not is_right_guess):
      guess = query_guess()

      if (guess in self.secret_word):
        self.update_right_letters(guess)
      else:
        wrong_guesses += 1
        display_hangman(wrong_guesses)
      
      out_of_guesses = wrong_guesses == total_guesses
      is_right_guess = not '_' in self.right_letters
      self.display_word_letters()
      display_avaible_guesses(wrong_guesses, total_guesses)

    if (is_right_guess):
      display_winner_message()
    else:
      display_loser_message(self.secret_word)

    self.end()

  def update_right_letters(self, guess):
    index = 0
    for letter in self.secret_word:
      if (guess == letter):
        self.right_letters[index] = letter

      index += 1

  def end(self):
    pass

  def display_word_letters(self):
    print(self.right_letters)


def display_avaible_guesses(wrong_guesses, total_guesses):
  avaible_guesses = total_guesses - wrong_guesses
  guess_text = 'guess' if avaible_guesses == 1 else 'guesses'

  print(f'You have {avaible_guesses} {guess_text}')

def display_welcome():
  print('**********************************')
  print('Welcome to hangman game in Python!')
  print('**********************************')

def query_guess():
  guess_input = input('Guess a letter: ')
  return guess_input.strip().upper()

def display_loser_message(secret_word):
    print("Damn, you are hanged!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def display_winner_message():
    print("Congratulations, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def display_hangman(wrong_guesses):
    print("  _______     ")
    print(" |/      |    ")

    if(wrong_guesses == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(wrong_guesses == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(wrong_guesses == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(wrong_guesses == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(wrong_guesses == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(wrong_guesses == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (wrong_guesses == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()