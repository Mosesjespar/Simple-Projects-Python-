import random

trials = 10
guess_length = 3

intro = f''' Bagels, a deductive logic game.
            By Al Sweigart al@inventwithpython.com
I am thinking of a {guess_length}-digit number with no repeated digits. Try to guess what it is. Here are some clues:
When I say:     That means:
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct'''


def getSecretNum():
    secretNum = ''
    nums = list('0123456789')
    random.shuffle(nums)
    for i in range(guess_length):
        secretNum += nums[i]
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You\'ve got it right!!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bargels'
    else:
        clues.sort()
        return ''.join(clues)


def main():
    print(intro)
    while True:
        # The main Loop
        # This stores the secret number the player needs to guess
        secretNum = getSecretNum()
        print(f'I have thought of a Number')
        print(f'You have {trials} guesses to get it right')
        numGuesses = 1
        while numGuesses <= trials:
            guess = ''
            # Looping until I get a Valid Input
            while len(guess) != guess_length or not guess.isdecimal():
                print(f'Guess {numGuesses}')
                guess = input('>>> ')
            # Displaying The Result
            clues = getClues(guess, secretNum)
            print(clues, end='\n')
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses > trials:
                print('You ran out of chances')
                print(f'The correct guess was {secretNum}')

        print('Do You Want to Play Again? (YES OR NO)')
        if not input('>>> ').lower().startswith('y'):
            # If true, we break out of the main loop
            break
    print('Thanks For Playing')


if __name__ == '__main__':
    main()
