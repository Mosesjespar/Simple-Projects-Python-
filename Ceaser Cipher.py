import pyperclip

intro = '''
CEASER CIPHER BY MOSES JESPAR
'''

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print(intro)

    while True:
        print('Do you want to encrypt(e) or decrypt (d)')
        response = input('>>> ')
        if response.lower().strip().startswith('e'):
            mode = 'encrypt'
            break
        elif response.lower().strip().startswith('d'):
            mode = 'decrypt'
            break
    while True:
        max_key = len(SYMBOLS) - 1
        print(f'Enter key to use 0-{max_key}')
        key_response = input('>>>  ')
        if not key_response.isdecimal():
            continue
        if 0 <= int(key_response) <= max_key:
            key = int(key_response)
            break
    print(f'Enter message to {mode}')
    message = input('>')
    message = message.upper()
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            if num >= len(SYMBOLS):
                num = num - len(SYMBOLS)
            elif num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print(translated)
    try:
        pyperclip.copy(translated)
        print(f'Full {mode}ed text copied to clipboard')
    except:
        pass


if __name__ == '__main__':
    main()
