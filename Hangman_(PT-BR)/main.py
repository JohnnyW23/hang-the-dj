from validador import inicio, letraValid, letraEscolhida, resultado
from objetos import titulo, processo, letras_ditas, hangman, erros, oculto

titulo()

secreta = inicio()

processo(secreta)

while True:
    
    erro = hangman(erros)
    
    letra = letraValid(letras_ditas)

    erro = letraEscolhida(letra)

    if erro:
        erros += 1
    
    if resultado(oculto, erros, secreta):
        print()
        break
