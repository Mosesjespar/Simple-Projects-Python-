import datetime
import random

start_year = datetime.date(2001, 1, 1)

intro = '''Birthday Paradox, by Al Sweigart al@inventwithpython.com
     The Birthday Paradox shows us that in a group of N people, the odds
     that two of them have matching birthdays is surprisingly large.
     This program does a Monte Carlo simulation (that is, repeated random simulations) 
     to explore this concept.
     (It's not actually a paradox, it's just a surprising result.)'''


def get_Birthdays(number_of_birthdays):
    birthday_list = []
    for i in range(number_of_birthdays):
        random_number_of_days = datetime.timedelta(random.randint(0, 365))
        birthday = start_year + random_number_of_days
        birthday_list.append(birthday)
    return birthday_list


def get_Match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    else:
        for a, i in enumerate(birthdays):
            for b, j in enumerate(birthdays[a + 1:]):
                if i == j:
                    return i


print(intro)
Months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
while True:  # Keep asking until the user enters a valid amount
    print('How many birthdays do you want me to Generate? (max 100) ')
    ans = input('>>  ')
    if ans.isdecimal() and (0 < int(ans) <= 100):
        numBdays = int(ans)
        break

print()
print(f'Here are {numBdays} Birthdays')
birthdays = get_Birthdays(numBdays)
