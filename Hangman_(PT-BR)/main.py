from validador import inicio, letraValid, letraEscolhida, resultado, playAgain
from objetos import titulo, processo, hangman, exit

titulo()

while True:
    secreta, letras_ditas, lista_secreta, oculto, erros = inicio()

    processo(secreta, lista_secreta, oculto)

    while True:
        
        erro = hangman(letras_ditas, oculto, erros)
        
        letra = letraValid(letras_ditas)

        erro = letraEscolhida(letra, letras_ditas, lista_secreta, oculto)

        if erro:
            erros += 1
        
        if resultado(letras_ditas, oculto, erros, secreta):
            print()
            break
    
    if not playAgain():
        exit()
        break
