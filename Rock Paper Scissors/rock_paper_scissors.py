import random

possible_choices = ['Rock', 'Paper', 'Scissors']
choices_input = {'R': 'Rock',  'P': 'Paper', 'S': 'Scissors'}
result = ''

print('Welcome to Rock. Paper. Scissors !')
print('Enter your decision ! [R : Rock, P : Paper, S : Scissors]')

player_choice = choices_input[input('> ')]
cpu_choice = random.choice(possible_choices)

print(f'----> Player chooses {player_choice}')
print(f'----> CPU chooses {cpu_choice}')

if player_choice == cpu_choice:
    print('**Draw!**')
elif player_choice == 'Rock' and cpu_choice == 'Paper':
    print('**CPU wins!**')
elif player_choice == 'Paper' and cpu_choice == 'Rock':
    print('**Player wins!**')
elif player_choice == 'Scissors' and cpu_choice == 'Rock':
    print('**CPU wins!**')
elif player_choice == 'Rock' and cpu_choice == 'Scissors':
    print('**Player wins!**')
elif player_choice == 'Paper' and cpu_choice == 'Scissors':
    print('**CPU wins!**')
elif player_choice == 'Scissors' and cpu_choice == 'Paper':
    print('**Player wins!**')
