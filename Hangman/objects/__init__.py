typed_letters = []

list_secret = []

hidden = []

errors = 0


def title():
    print(f'''\033[36m
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
{'HANGMAN v1.0'.center(41)}
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
\033[m''')


def process(secret):

    for l in secret:
        list_secret.append(l)

    for l in secret:
        hidden.append('_')


def previousLetters():
    for i, l in enumerate(typed_letters):
        if i == 0:
            print(l, end='')
        else:
            print(f' - {l}', end='')
    
    print()


def hangman(errors):
    
    previousLetters()

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
