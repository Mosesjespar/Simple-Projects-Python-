import sys
import time


def main():
    print('Enter a number to start with or Quit')
    while True:
        response = input('>> ')
        if response.isdecimal() and int(response) != 0:
            num = int(response)
            break
        if response.lower().startswith('q'):
            print('Thanks for Playing')
            sys.exit()
        print('Please Enter a Number > 0 or q to Quit')

    print(num, end=' ', flush=True)
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 1 + (3 * num)
        print(f'{num}', flush=True, end=' ')
        time.sleep(0.5)


if __name__ == '__main__':
    main()
