def start():
    from words import words
    from objects import title
    from random import choice
    from time import sleep

    sleep(1)

    while True:
        answer = input('Would you like to choose the game secret word? \033[33m[Y/N]\033[m: ').upper().strip()

        if answer == 'Y':
            secret = secretValid()
            for _ in range(0, 50):
                print()
            title()
            return secret

        elif answer == 'N':
            secret = choice(words).upper()
            print('Random word chosen from list...')

            sleep(2)
            return secret

        else:
            print('\033[31mChoose a valid answer!\033[m')


def secretValid():
    while True:
        secret = input('Type the game secret word: ').upper().strip()

        if secret.isalpha():
            return secret
        
        else:
            print('\033[31mType a WORD!\033[m')


def letterValid(typed):
    from time import sleep
    
    sleep(1)
    print()

    while True:
        letter = input('Choose a letter: ').upper().strip()

        if letter in typed:
            print('\033[33mYou already typed this letter before!\033[m')
        
        elif len(letter) > 1 and letter.isalpha():
            print('\033[31mType ONE letter ONLY!\033[m')

        elif letter.isalpha() and len(letter) == 1:
            print('''\033[36m
=========================================
\033[m''')
            return letter
        
        else:
            print('\033[31mType a LETTER!\033[m')


def chosenLetter(letter):
    from objects import typed_letters, list_secret, hidden
    from time import sleep

    typed_letters.append(letter)

    if letter not in list_secret:
        print(f'There is no \033[33m{letter}\033[m!')
        sleep(1)
        print()
        return True

    else:
        print(f'\033[32mYou found a letter!\033[m')
        sleep(1)
        print()
        for i, l in enumerate(list_secret):
            if letter == l:
                hidden.pop(i)
                hidden.insert(i, f'\033[33m{l}\033[m')


def results(hidden, errors, secret):
    from objects import hangman

    if '_' not in hidden:
        hangman(errors)
        print()
        print()
        print('\033[32mCongratulations! You won.\033[m')
        return True

    if errors == 6:
        hangman(errors)
        print()
        print()
        print(f'\033[31mYou lose! The word is \033[33m{secret}\033[m')
        return True

    return False