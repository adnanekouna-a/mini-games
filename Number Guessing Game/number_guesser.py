import random


def try_message(n_tries:int) -> str:
    '''Adjust the word try to plural or singular'''
    gram = ''
    if n_tries == 1:
        gram = 'try'
    else:
        gram = 'tries'
    return f'You got it from {n_tries} {gram}!'


print('''
Hello!
Welcome to NGG!
Version 1.0.1
''')

print('''Select difficulty:
-> Easy (from 0 to 100) [1]
-> Medium (from 0 to 1000) [2]
-> Hard (from 0 to 10000) [3]
''')

# Fix blank or unvailable difficulty
while True:
    difficulty = input('> ')
    if difficulty in ['1', '2', '3']:
        break
    print('Unavailable Difficulty!')

TRIES = 0

if difficulty == '1':
    number = random.randint(0, 100)
elif difficulty == '2':
    number = random.randint(0, 1000)
elif difficulty == '3':
    number = random.randint(0, 10000)

while True:
    guess = int(input('Guess : '))
    if guess > number:
        print('Lower')
        TRIES += 1
    elif guess < number:
        print('Higher')
        TRIES += 1
    elif guess == number:
        TRIES += 1
        print('Bingo! You got it')
        print(try_message(TRIES))
        break
