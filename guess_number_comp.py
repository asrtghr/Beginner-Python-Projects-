import random

def welcome():
  '''
  A simple introduction console output to user select a giving difficult
  '''
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
  '''
  receive a guessed number from user and shows how close the number are from the random number
  if the guessed number corresponds to the random number, return a congratulations output
  '''
  config = [(20,5), (100,10), (500,15), (1000,25)]

  interval , trials = config[diff] 

  rn_number = random.randint(0,interval)

  while trials:
    guess = int(input(f"Guess a number between 0 and {interval} \n"))
    
    if guess < rn_number:
      trials -= 1
      print(f"Sorry, guess again, too low")
    elif guess > rn_number:
      trials -= 1
      print(f"Sorry, guess again, too high")
    else:
      return f"Yaay, congrats. You have guessed the number {rn_number} correctly"
    
    print(f"YOU HAVE {trials} TRIALS LEFT\n")
  
  print(f"Too bad... looks like you didn't guessed the correct number, try again!")
  print(f"The random number was {rn_number}")


if __name__ == '__main__':
  welcome()
  
  diff = int(input("> "))
  if diff not in [0,1,2,3]:
    print('SELECT A GIVING DIFFICULT')
    diff = int(input("> "))
    
  guess(diff)
