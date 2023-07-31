import random

# Create a list of play options
computer_choice = ['rock', 'paper', 'scissors']

def RPS():
    input("Welcome to Rock, Paper, Scissors! Press Enter to begin.")
    print("Please choose either rock, paper, or scissors.")

    while True:
        user_choice = input("Rock, Paper, or Scissors? ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Please enter a valid move.")
        else:
            break

    random_choice = random.choice(computer_choice)

    # Define the winning conditions using a dictionary
    outcomes = {
        'rock': {'rock': 'It\'s a tie!',
                'scissors': 'You win!', 
                'paper': 'You lose!'},

        'paper': {'rock': 'You win!',
                 'scissors': 'You lose!',
                 'paper': 'It\'s a tie!'},
                 
        'scissors': {'rock': 'You lose!',
                    'scissors': 'It\'s a tie!',
                      'paper': 'You win!'}
    }

    print(f"Your choice: {user_choice}, computer choice: {random_choice}")
    print(outcomes[user_choice][random_choice])


RPS()