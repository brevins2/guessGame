print('******* Welcome to a Guessing Game *******\n')


def guessgame():
    guess = 'Brevin'
    age = 23
    country = 'Uganda'
    numberOfGuesses = 0

    while numberOfGuesses <= 10:
        yourGuess = input('Enter your Guess: ')
        if yourGuess == guess:
            print('Name guess ' + yourGuess + ' is correct')
        else:
            print('incorrect guess ' + yourGuess + ' try again later -> ' + str(numberOfGuesses) + '\n')
            numberOfGuesses = numberOfGuesses + 1
            continue

        yourAge = input('Enter age: ')
        if str(age) == yourAge:
            print('Age guess ' + yourAge + ' is correct')
        else:
            print('incorrect age guess ' + yourAge + ' is incorrect -> ' + str(numberOfGuesses) + '\n')
            numberOfGuesses = numberOfGuesses + 1
            continue

        yourCountry = input('Enter country of residence: ')
        if yourCountry == country:
            print('Country guess ' + yourCountry + ' is correct')
            break
        else:
            print('incorrect country guess ' + yourCountry + ' is incorrect -> ' + str(numberOfGuesses) + '\n')
            numberOfGuesses = numberOfGuesses + 1
            continue

    print('\n\ncongratulations, you know Kiggundu Brevin well\n')


guessgame()
