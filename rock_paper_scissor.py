import random

def introduce():
  print(f"*" + f"=-" * 30 + f"*")
  intro = 'WELCOME TO ROCK PAPER SCISSOR GAME'
  print(f"|" + intro.center(60, " ") + f"|")
  difficults = ['SELECT ONE OPTION',
                'ROCK', 
                'PAPER',
                'SCISSOR',]
  for diff in difficults:
    print(f"|" + diff.center(60, " ") + f"|")
  print(f"*" + f"-=" * 30 + f"*")

def play(user_input):
  select = random.choice(['ROCK','PAPER','SCISSOR'])

  if user_input == select:
    print(f"TIE")
  result = is_win(user_input, select)
  print(result)

def is_win(user, computer):
  if user == 'ROCK' and computer == 'SCISSOR' or user == 'PAPER' and computer == 'ROCK' or user == 'SCISSOR' and computer == 'PAPER':
    return f"Congratulations, You Won!!\nYou chose {user} and the computer chose {computer}"
  return f"You Lost :/\nYou chose {user} and the computer chose {computer}"

def main():
  introduce()
  user_input = input("> ")
  play(user_input)

main()
