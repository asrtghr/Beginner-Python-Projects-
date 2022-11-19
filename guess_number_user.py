import random, time

def welcome():
  print(f"*" + f"=-" * 30 + f"*")
  intro = 'SELECT THE DIFFICULT'
  print(f"|" + intro.center(60, " ") + f"|")
  difficults = ['EASY(0): RANDOM NUMBER (0-20) / 5 CHANCES', 
                'MEDIUM(1): RANDOM NUMBER (0-100) / 10 CHANCES', 
                'HARD(2): RANDOM NUMBER (0-500) / 15 CHANCES', 
                'EXTREME(3): RANDOM NUMBER (0-1000) / 25 CHANCES']
  for diff in difficults:
    print(f"|" + diff.center(60, " ") + f"|")
  print(f"*" + f"-=" * 30 + f"*")

def guess(diff):
  config = [(20,5), (100,10), (500,15), (1000,25)]

  feedback = 0
  start = 0

  guessed_numbers = []
  interval , trials = config[diff] 

  print(f"Computer: Select a number to be guessed")

  user_number = int(input("> "))

  while feedback != 3:

    guess = random.randint(start,interval) 

    if guess in guessed_numbers:
      guess = random.randint(start,interval)
    else:
      guessed_numbers.append(guess)

    feedback = int(input(f"Is {guess}, too High (1), too Low(2) or correct(3)"))

    if feedback == 1:
      interval -= guess - user_number
      trials -= 1
    elif feedback == 2:
      start = guess
      trials -= 1
    
    print(f'Computer: I still have {trials} trials left.')

  print(f"Computer: Yay, I guessed your number, {guess}, correctly")   

if __name__ == '__main__':
  welcome()
  print('COMPUTER: Let\'s choose a difficult')
  time.sleep(3)
  rn_cmp_choice = random.randint(0,3)
  diff = ['Easy', 'Medium', 'Hard', 'Extreme']
  print(f'Computer: I think i\'m gonna go on {diff[rn_cmp_choice]} mode')
  time.sleep(3)
  guess(rn_cmp_choice)
