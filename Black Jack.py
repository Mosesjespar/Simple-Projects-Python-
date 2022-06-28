import sys
import random

# Set up the constants:
HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.
# 15. # (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

intro = '''
Blackjack, by Moses Jespar , mosesjespar@gmail.com
Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.'''


def getBet(maxBet):
    # Ask the player how much they want to bet for this round.
    while True:  # loop until the user enters a valid input
        print(f'How much do you want to bet,(1-{maxBet}, or QUIT)')
        bet = input('>>> ').upper().strip()
        if bet == 'QUIT':
            sys.exit()
        if not bet.isdecimal():
            continue  # the player entered a number
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player entered a valid bet.


def getDeck():
    # returning a list of tuples
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # adding numbered cards
        for rank in ('J', 'Q', 'A', 'K'):
            deck.append((rank, suit))  # adding face cards and the ace
    random.shuffle(deck)
    return deck


def getHandValues(cards):
    value = 0
    num_of_aces = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':  # getting the number of aces
            num_of_aces += 1
        elif rank in ('J', 'K', 'Q'):  # adding value of face cards
            value += 10
        else:  # if only numbered cards are found
            value += int(rank)
    value += num_of_aces  # each ace adds to 1
    for i in range(num_of_aces):
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(cards):
    # display all cards in the card list
    rows = ['', '', '', '', ]
    for i, card in enumerate(cards):
        rows[0] += ' ___ '  # printing the top of the card
        if card == BACKSIDE:
            # printing the back of the card
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            # displaying the front of the card
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def displayHands(pHand, dHand, showD_Hand):
    # showing both dealer and player hands if showD_Hand is true
    if showD_Hand:
        print('DEALER: ', getHandValues(dHand))
        displayCards(dHand)
    else:
        print('DEALER: ???')
        # hide the dealers]'s first card
        displayCards([BACKSIDE] + dHand[1:])
    print('PLAYER: ', getHandValues(pHand))
    displayCards(pHand)


def getMove(playerHand, money):
    while True:  # keep looping until the player enters a valid input
        moves = ['(H)it', '(S)tand']
        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        movePrompt = ', '.join(moves) + '>>  '
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move  # Player has entered a valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Player has entered a valid move.


def main():
    money = 5000
    print(intro)
    while True:  # checking if the player has run out of money
        if money <= 0:
            print('You are broke')
            print('Good thing it was not real money')
            print('Thanks for playing')
            sys.exit()

        # Let the player enter their bet for this round:
        print(f'Money: {money}')
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # handling player actions
        print(f'Bet: {bet}')
        while True:  # keep looping until the player stands or bursts
            displayHands(player_hand, dealer_hand, False)
            print()

            # check if a player is bust
            if getHandValues(player_hand) > 21:
                break

            # get player move
            move = getMove(player_hand, money - bet)
            if move == 'D':
                # Player is doubling down, they can increase their bet
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print(f'Bet increased to {bet}')
                print('Bet: ', bet)
            if move in ('H', 'D'):  # Hit/doubling down takes another card
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}')
                player_hand.append(new_card)
                if getHandValues(player_hand) > 21:
                    continue
            if move in ('S', 'D'):  # Stand/doubling down stops the player's turn
                break
        # handling dealer's actions
        if getHandValues(player_hand) < 21:
            while getHandValues(dealer_hand) < 17:
                # the dealer hits
                print('The Dealer hits...')
                dealer_hand.append(deck.pop())
                displayHands(player_hand, dealer_hand, False)

                if getHandValues(dealer_hand) > 21:
                    break  # the dealer has busted
                input('Press enter to continue...')
                print()
                print()
        displayHands(player_hand, dealer_hand, True)

        player_value = getHandValues(player_hand)
        dealer_value = getHandValues(dealer_hand)
        # Handle whether the player won, lost, or tied:
        if dealer_value > 21:
            print(f'The dealer busts! You win ${bet}')
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print(f'You Lost!!...')
            money -= bet
        elif player_value > dealer_value:
            print(f'You Won ${bet}')
            money += bet
        elif player_value == dealer_value:
            print('It is a tie, the money is returned to you.')
        input('Press enter to continue')


if __name__ == '__main__':
    main()
