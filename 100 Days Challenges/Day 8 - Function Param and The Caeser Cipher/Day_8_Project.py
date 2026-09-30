# the goal of this project is to create Caeser Cipher

# setup
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
len_letters = len(letters)

def encrypt(shift, message):
    cipher = ''

    for letter in message:
        if letter in letters:
            # encrypting only the letters
            index_num = letters.index(letter) + shift
            if index_num > len_letters - 1:
                index_num %= len_letters            # makes sure we stay in the range of our list no matter what.
            cipher += letters[index_num]
        else:
            # any symobls or spaces will not be encoded.
            cipher += letter

    print(f'here is your encrypted text: {cipher}')

def decrypt(shift, text):
    decoded = ''

    for letter in text:
        if letter in letters:
            # decrypting only the letters.
            index_num = letters.index(letter) + (shift * len_letters - shift)
            if index_num > len_letters - 1:
                index_num %= len_letters
            decoded += letters[index_num]
        else:
            # any symbols or spaces will be returned as is.
            decoded += letter

    print(f'here is your decrypted text: {decoded}')

# the cipher

def caeser(mode):
    if mode == 'encode':
        encrypt(int(shift), text)
    elif mode == 'decode':
        decrypt(int(shift), text)
    else:
        print('invalide input')

script_state = True

while script_state:

    mode = input('type \'encode\' to encode a message and type \'decode\' to decode a message.\n')
    text = input('please type in your text.\n')
    shift = input('please type the shift number.\n')

    caeser(mode)

    user_exit = input('do you want to exit the cipher or no? [y] or [n]\n')[0].lower()

    if user_exit == 'y':
        script_state = False

# I didn't follow the instructor's code as I tried to do it myself, she delibertly made sure that a bug is there in her code, however, my code doesn't have that bug which I guess is great!
