def title():
    print(f'''\033[36m
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
{'HANGMAN v1.0'.center(41)}
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
\033[m''')


def process(secret, list_secret, hidden):

    for l in secret:
        list_secret.append(l)

    for l in secret:
        if l == '-':
            hidden.append('-')
        elif l == ' ':
            hidden.append(' ')
        else:
            hidden.append('_')


def previousLetters(typed_letters):
    for i, l in enumerate(typed_letters):
        if i != 0 and i % 2 == 0 and i % 5 == 0:
            print('\n')
        if i % 2 == 0 and i % 5 == 0:
            print(l, end='')
        else:
            print(f' - {l}', end='')
    
    print()


def hangman(typed_letters, hidden, errors):
    
    previousLetters(typed_letters)

    h = t = la = ra = ll = rl = ' '
    if errors >= 1:
        h = '\033[31mO\033[m'
    if errors >= 2:
        t = '\033[31m|\033[m'
    if errors >= 3:
        la = '\033[31m/\033[m'
    if errors >= 4:
        ra = '\033[31m\\\033[m'
    if errors >= 5:
        ll = '\033[31m/\033[m'
    if errors == 6:
        rl = '\033[31m\\\033[m'
    
    print(f'''
             ________
            /        \\
            |         {h}
            |        {la}{t}{ra}
            |        {ll} {rl}
            |
        ____|______________
        
        ''', end='')

    for l in hidden:
        print(l, end=' ')
    
    print()
    return False


def exit():
    from time import sleep
    print('''\033[36m
=========================================

<<< THANK YOU FOR PLAYING HANGMAN! UNTIL NEXT TIME :) >>>
\033[m''')
    sleep(1)
