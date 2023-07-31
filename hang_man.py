import json
import random

with open('words.json') as f:
    words = json.load(f)

random_word = random.choice(words['data'])

def hang_man():
    counter = 0
    print('random word will be generated')
    length_of_word = len(random_word)
    print(f'word length is {length_of_word}')
    print(f'you have {length_of_word} chances to guess the word')
    
    while counter < length_of_word:
        user_input = input('enter a letter\n')
        
        if user_input in random_word:
            print('correct')
            
        else:
            print('wrong')
            counter += 1


hang_man()
