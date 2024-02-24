letras_ditas = []

lista_secreta = []

oculto = []

erros = 0


def titulo():
    print(f'''\033[36m
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
{'JOGO DA FORCA v1.0'.center(41)}
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
\033[m''')


def processo(secreta):

    for l in secreta:
        lista_secreta.append(l)

    for l in secreta:
        if l == '-':
            oculto.append('-')
        elif l == ' ':
            oculto.append(' ')
        else:
            oculto.append('_')


def letrasAnteriores():
    for i, l in enumerate(letras_ditas):
        if i == 0:
            print(l, end='')
        else:
            print(f' - {l}', end='')
    
    print()


def hangman(erros):
    
    letrasAnteriores()

    c = t = be = bd = pe = pd = ' '
    if erros >= 1:
        c = '\033[31mO\033[m'
    if erros >= 2:
        t = '\033[31m|\033[m'
    if erros >= 3:
        be = '\033[31m/\033[m'
    if erros >= 4:
        bd = '\033[31m\\\033[m'
    if erros >= 5:
        pe = '\033[31m/\033[m'
    if erros == 6:
        pd = '\033[31m\\\033[m'
    
    print(f'''
             ________
            /        \\
            |         {c}
            |        {be}{t}{bd}
            |        {pe} {pd}
            |
        ____|______________
        
        ''', end='')

    for l in oculto:
        print(l, end=' ')
    
    print()
    return False
