import datetime

intro = '''
 Calender Maker by Moses Jespar
'''

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')
print(intro)
print()
while True:  # getting the calendar year
    print('Enter The Year of the calendar to use (4 digits)..')
    response1 = input('>> ')
    if response1.isdecimal() and int(response1) >= 1000:
        year = int(response1)
        break

while True:  # Getting the month to use
    print('Enter the month to use 1-12')
    response2 = input('>> ')
    if response2.isdecimal() and 1 <= int(response2) <= 12:
        month = int(response2)
        break


def getCalendarFor(year, month):
    calText = ''  # this will contain the string for our calendar
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..' + '\n'
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'
    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator
        # dayNumberRow is the row with the day number labels
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)  # Go to next day
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow
        if currentDate.month != month:
            break
    # Add the horizontal line at the very bottom of the calendar
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)
calendarFileName = f'Calendar_{year}_{month}.txt'
with open(calendarFileName, 'w') as cal:
    cal.write(calText)
print(f'{calendarFileName} saved')
