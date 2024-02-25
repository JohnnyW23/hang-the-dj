from validator import start, letterValid, chosenLetter, results, playAgain
from objects import title, process, hangman, exit

title()

while True:
    secret, typed_letters, list_secret, hidden, errors = start()

    process(secret, list_secret, hidden)

    while True:
        
        error = hangman(typed_letters, hidden, errors)
        
        letter = letterValid(typed_letters)

        error = chosenLetter(letter, typed_letters, list_secret, hidden)

        if error:
            errors += 1
        
        if results(typed_letters, hidden, errors, secret):
            print()
            break
    
    if not playAgain():
        exit()
        break
