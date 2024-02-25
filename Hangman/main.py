from validator import start, letterValid, chosenLetter, results
from objects import title, process, typed_letters, hangman, errors, hidden

title()

secret = start()

process(secret)

while True:
    
    error = hangman(errors)
    
    letter = letterValid(typed_letters)

    error = chosenLetter(letter)

    if error:
        errors += 1
    
    if results(hidden, errors, secret):
        print()
        break
