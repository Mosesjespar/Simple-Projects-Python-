import pyperclip

intro = '''
CEASER HACKER BY MOSES JESPAR
'''


def main():
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(intro)
    print('Enter encrypted Ceaser cipher text to hack')
    txt = input('>> ')
    txt = txt.upper()
    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in txt:
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(SYMBOLS)
                translated = translated + SYMBOLS[num]
            else:
                translated = translated + symbol
        print(f'Key #{key}:  {translated}')


if __name__ == '__main__':
    main()
