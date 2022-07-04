import random

intro = '''
Clickbait Program by Moses Jespar
'''
object_pronouns = ['Her', 'Him', 'Them']
possesive_pronouns = ['Her', 'His', 'Their']
personal_pronouns = ['She', 'He', 'They']
states = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina',
          'Michigan']
nouns = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
places = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
when = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def generateAreMillennialsKillingHeadline():
    Noun = random.choices(nouns)
    Noun = ''.join(Noun)
    return f'Are Millennials Killing the {Noun} Industry?'


def generateWhatYouDontKnowHeadline():
    Noun = random.choices(nouns)
    Noun = ''.join(Noun)
    plural_noun = random.choices(nouns)
    plural_noun = ''.join(plural_noun)
    When = random.choices(when)
    When = ''.join(When)
    return f'Without this {Noun}, {plural_noun}s could kill You {When}'


def generateBigCompaniesHateHeadline():
    pronoun = random.choice(object_pronouns)
    pronoun = ''.join(pronoun)
    state = random.choice(states)
    state = ''.join(state)
    noun1 = random.choice(nouns)
    noun1 = ''.join(noun1)
    noun2 = random.choice(nouns)
    noun2 = ''.join(noun2)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}'


def generateYouWontBelieveHeadline():
    State = random.choice(states)
    State = ''.join(State)
    Noun = random.choice(nouns)
    Noun = ''.join(Noun)
    Pronoun = random.choice(possesive_pronouns)
    Pronoun = ''.join(Pronoun)
    Place = random.choice(places)
    Place =''.join(Place)
    return f'You Won\'t Believe What This {State} {Noun} Found in {Pronoun} {Place}'


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(nouns) + 's'
    pluralNoun2 = random.choice(nouns) + 's'
    return f'What {pluralNoun1} Don\'t Want You To Know About {pluralNoun2}'


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    Noun = random.choice(nouns)
    State = random.choice(states)
    Noun = ''.join(Noun)
    return f'{number} Gift Ideas to Give Your {Noun} From {State}'


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(nouns) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return f"{number1} Reasons Why {pluralNoun} Are More Interesting Than You Think (Number {number2} Will Surprise " \
           f"You!) "


def generateJobAutomatedHeadline():
    State = random.choice(states)
    Noun = random.choice(nouns)
    i = random.randint(0, 2)
    pronoun1 = possesive_pronouns[i]
    pronoun2 = possesive_pronouns[i]
    Noun = ''.join(Noun)
    if pronoun1 == 'Their':
        return f'This {State} {Noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong.'
    else:
        return f'This {State} {Noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong.'


def main():
    print(intro)
    print()
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of head lines to create.')
        response = input('>> ')
        if not response.isdecimal():
            print('Enter a number')
        else:
            num_head_lines = int(response)
            break
    for i in range(num_head_lines):
        clickbaitType = random.randint(1, 8)
        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()
        print(headline)
    print()
    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    When = random.choice(when).lower()
    print('Post these to our', website, When, 'or you\'re fired!')


if __name__ == '__main__':
    main()
