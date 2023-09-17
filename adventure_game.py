# Adventure game!!!
import time
import random
import os
import characters


arena = random.choice(characters.arenas)
arena_attribute = random.choice(characters.arena_attributes)
# character = random.choice(characters.characters)
weapon = random.choice(characters.weapons)
housing = random.choice(characters.housings)
housing2 = random.choice(characters.housings2)
antagonist = random.choice(characters.antagonists)
lucky_number = random.randint(1, 2)
choices = ['1', '2']
playing = True
is_weaponized = False


def output_message(msg):
    print(msg)
    time.sleep(2)


def valid_input(msg, first_choice, second_choice):
    choice = input


def check_luck(lucky_number):

    checking = True
    output_message('Shall we check your luck '
                   'before you start the adventure?')

    while checking:
        luck = input('Please enter "yes" to check'
                     ' or "no" to skip: ').lower()
        if luck == 'yes':
            while True:
                number = (input('pick a number between 1 and 2: '))
                if number not in choices:
                    print('Invalid input')
                    continue
                else:
                    if int(number) == lucky_number:
                        output_message('We are starting with alot of luck')
                        return
                    else:
                        output_message('This is a bad luck to start with!')
                        return
        elif luck == 'no':
            checking = False
        else:
            print('Invalid input!')
            continue


def intro(arena, arena_attribute, housing, housing2, antagonist):
    output_message('\n\nWelcome to the game!!!')
    output_message(
        f'You find yourself {arena}, surrounded with {arena_attribute}.')
    output_message(f'Rumor has it that a {antagonist} is somewhere around,'
                   'and has been terrifying the whole area!')
    output_message(f'In front of you is a white {housing}.')
    output_message(f'To your right is a black {housing2}.')
    output_message('In your hand you hold your trusty'
                   '(but not very effective) dagger.\n\n')
    output_message(f'Enter 1 to go into the {housing}')
    output_message(f'Enter 2 to go into the {housing2}')


def win():
    output_message(f'As the {antagonist} attacked you,'
                   ' you fought with your new weapon and killed it')
    output_message(f'Yay, you are victorious...\nCONGRATULATIONS!!!...')
    play_again()


def lose():
    output_message(f'As the {antagonist} attacked you,'
                   'your weak dagger was not enough to defeat it')
    output_message(f'The {antagonist} just ate you alive...\nYOU LOST!!!')
    play_again()


def go_back():
    output_message(f'you are back on the {arena}')
    output_message(f'Enter 1 to go into the {housing}')
    output_message(f'Enter 2 to go into the {housing2}')


def meet_antagonist(weaponized):
    output_message(f'You entered the {housing}')
    output_message(f'it is the {antagonist} resident')
    output_message(f'the {antagonist} attacks you')
    while True:
        decision = input('Would you like to 1. fight or 2. run away\n'
                         'Please enter 1 or 2: ')
        if decision == choices[0] and weaponized:
            win()
        elif decision == choices[0] and not weaponized:
            lose()
        elif decision == choices[1]:
            output_message('You decided to run away!')
            output_message('luckily you seemed not to be followed')
            go_back()
            break
        else:
            print('Invalid input')
            continue


def get_weapon():
    output_message(f'you moved hastily to the {housing2}!')
    output_message(
        f'you saw a box, opened it and found a beautiful {weapon}')
    go_back()


def play_again():
    while True:
        choice = input(
            'Would you like to play again? Enter yes or no\n').lower()
        if choice == 'yes':
            arena = random.choice(characters.arenas)
            arena_attribute = random.choice(characters.arena_attributes)
            weapon = random.choice(characters.weapons)
            housing = random.choice(characters.housings)
            housing2 = random.choice(characters.housings2)
            antagonist = random.choice(characters.antagonists)
            lucky_number = random.randint(1, 2)
            is_weaponized = False
            os.system('clear')
            play_game(arena, arena_attribute, weapon,
                      housing, housing2, antagonist,
                      lucky_number, is_weaponized)
        elif choice == 'no':
            exit(1)
        else:
            print('Invalid input!')
            continue


def start_game(weaponized):
    choice = input('Please enter 1 or 2: ')
    if choice not in choices:
        start_game(weaponized)
    elif choice == choices[0]:
        meet_antagonist(weaponized)
        start_game(weaponized)
    elif choice == choices[1]:
        weaponized = True
        get_weapon()
        start_game(weaponized)


def play_game(arena, arena_attribute, weapon,
              housing, housing2, antagonist, lucky_number, is_weaponized):
    output_message('Hello Player!!!')
    check_luck(lucky_number)
    intro(arena, arena_attribute, housing, housing2, antagonist)
    start_game(is_weaponized)


if __name__ == '__main__':
    play_game(arena, arena_attribute, weapon,
              housing, housing2, antagonist, lucky_number, is_weaponized)
