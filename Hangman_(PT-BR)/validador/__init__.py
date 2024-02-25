def inicio():
    from palavras import palavras
    from objetos import titulo
    from random import choice
    from time import sleep

    letras_ditas = []
    lista_secreta = []
    oculto = []
    erros = 0

    sleep(1)

    while True:
        resposta = input('Você deseja escolher a palavra do jogo? \033[33m[S/N]\033[m: ').upper().strip()

        if resposta == 'S':
            secreta = secretaValid()
            for _ in range(0, 50):
                print()
            titulo()
            return secreta, letras_ditas, lista_secreta, oculto, erros

        elif resposta == 'N':
            secreta = choice(palavras).upper()
            print('Palavra aleatória escolhida da lista...')

            sleep(2)
            return secreta, letras_ditas, lista_secreta, oculto, erros

        else:
            print('\033[31mEscolha uma alternativa válida!\033[m')


def secretaValid():
    from string import ascii_letters, digits
    char = ['-', ' ']
    for c in ascii_letters:
        char.append(c)
    for c in digits:
        char.append(c)

    while True:
        true = 0
        secreta = input('Digite a palavra do jogo: ').upper().strip()
        for l in secreta:
            if l in char:
                true += 1
        
        if true == len(secreta):
            return secreta
        
        else:
            print('\033[31mNÃO USE SÍMBOLOS PARA SUA PALAVRA/ESCOLHA UMA PALAVRA SEM ACENTO!\033[m')

def letraValid(ditas):
    from time import sleep
    
    sleep(1)
    print()

    while True:
        letra = input('Escolha uma letra: ').upper().strip()

        if letra in ditas:
            print('\033[33mVocê já disse essa letra antes!\033[m')
        
        elif len(letra) > 1:
            print('\033[31mDigite APENAS UMA letra!\033[m')

        elif len(letra) == 1 and letra.isalnum():
            print('''\033[36m
=========================================
\033[m''')
            return letra
        
        else:
            print('\033[31mDigite uma LETRA!\033[m')


def letraEscolhida(letra, letras_ditas, lista_secreta, oculto):
    from time import sleep

    letras_ditas.append(letra)

    if letra not in lista_secreta:
        print(f'Não existe \033[33m{letra}\033[m !')
        sleep(1)
        print()
        return True

    else:
        print(f'\033[32mVocê encontrou uma letra!\033[m')
        sleep(1)
        print()
        for i, l in enumerate(lista_secreta):
            if letra == l:
                oculto.pop(i)
                oculto.insert(i, f'\033[33m{l}\033[m')


def resultado(letras_ditas, oculto, erros, secreta):
    from objetos import hangman

    if '_' not in oculto:
        hangman(letras_ditas, oculto, erros)
        print()
        print()
        print('\033[32mParabéns! Você venceu o jogo.\033[m')
        return True

    if erros == 6:
        hangman(letras_ditas, oculto, erros)
        print()
        print()
        print(f'\033[31mVocê perdeu! A palavra era \033[33m{secreta}\033[m')
        return True

    return False


def playAgain():
    from time import sleep

    while True:
        resp = input('Jogar novamente? [S/N]: ').upper().strip()

        if resp != 'S' and resp != 'N':
            print('\033[31mDÊ UMA RESPOSTA VÁLIDA!\033[m')
        
        elif resp == 'N':
            return False
        
        else:
            print('''\033[33m
INICIANDO NOVO JOGO...
\033[m''')
            sleep(1)
            print('''\033[36m=========================================
\033[m''')
            return True
