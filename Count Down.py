import sevseg
import time


def main():
    seconds_left = 30
    while True:
        print('\n' * 6)
        hours = str(seconds_left // 3600)
        mins = str((seconds_left % 3600) // 60)
        secs = str(seconds_left % 60)

        # Get the digit strings from the sevseg module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(mins, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(secs, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(hTopRow + ' ' + mTopRow + ' ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)

        if seconds_left == 0:
            print()
            print(' * * * * BOOM * * * *')
            break
        print()
        print('Press Ctrl-C to quit.')
        time.sleep(1)  # Insert a one-second pause.
        seconds_left -= 1


if __name__ == '__main__':
    main()
