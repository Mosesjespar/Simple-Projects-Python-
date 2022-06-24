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
    for j in range(number_of_birthdays):
        # generating days to add on the start year
        random_number_of_days = datetime.timedelta(random.randint(0, 365))
        created_bd = start_year + random_number_of_days
        birthday_list.append(created_bd)
    return birthday_list


def get_Match(bds):
    if len(bds) == len(set(bds)):  # Looking for similar birthdays
        return None
    else:
        # comparing each birthday within the created list
        for a, bd1 in enumerate(bds):
            for b, bd2 in enumerate(bds[a + 1:]):
                if bd1 == bd2:
                    return bd1


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

for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
        month_name = Months[birthday.month - 1]
        date_text = f'{month_name, birthday.day}'
        print(date_text, end='')
print()
print()

# Determine if there are two birthdays that match
match = get_Match(birthdays)
print('In this simulation, ', end='')
if match is not None:
    # getting the bd month of th match
    month_name = Months[match.month - 1]
    date_text = f'{month_name, match.day}'
    print(f'Multiple people have a birthday on {date_text}')
else:
    print('No matching Birthdays where found')

# Generating 100,000 simulations
print(f'Generating {numBdays} birthdays 100,000 times')
input('Press Enter to Begin')
simMatch = 0  # How many simulations had matching birthdays in them
for i in range(100000):
    if i % 10000 == 0:
        print(f'{i} simulations run....')
    birthdays = get_Birthdays(numBdays)
    if get_Match(birthdays) is not None:
        simMatch = simMatch + 1
print(f'100000 simulations run.....')
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
print(simMatch)
