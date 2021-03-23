# substitution cipher by Hayden Dennison
# adds a newline to the ciphertext which shows up as a random character
# in decryption
# to decrypt pass the ciphertext as plaintext and key as 126-key
import argparse

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]\
^_`a bcdefghijklmnopqrstuvwxyz{|}~\n'
WRAP = len(LETTERS)
WORDS = set()
with open("english_words.txt") as word_file:
    WORDS = set(word.strip().lower() for word in word_file)
# Encrypts and returns a plaintext using a Caesar cipher
def encrypt_caesar(plainText, key):
    global LETTERS, WRAP
    cipherText = ''
    for char in plainText:
        s = LETTERS.index(char)+key
        if s >= WRAP:
            s = s - WRAP
        cipherText = cipherText + LETTERS[s]
    return cipherText

# This function and the code for creation of the WORDS set was taken 
# from StackOverflow user kindall
def is_english_word(word):
    global WORDS
    return word.lower() in WORDS

# Evaluate how similar a given text is to English.
def get_fitness(text):
    base = len(text.split(' '))
    num = 0
    for word in text.split(' '):
        num = num + int(is_english_word(word))
    return float(num)/base

def get_parser():
    parser = argparse.ArgumentParser(\
                description='Encrypt/crack a message in caesar cipher.')
    parser.add_argument('-p', '--plaintext', type=str, action='store', \
                        help='The filename of the plaintext file.', \
                        default=None)
    parser.add_argument('-c', '--ciphertext', type=str, action='store', \
                        help='The filename of the ciphertext file.', \
                        default=None)
    parser.add_argument('-k', '--key', type=int, action='store', \
                        help='The key. (a number)', default=0)
    parser.add_argument('-cr', '--crack', type=bool, action='store', \
                        help='Crack the text in the ciphertext file.',default=0)
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    plainText = ''
    cipherText = ''
    cipherFilename = args.ciphertext
    while cipherFilename == None:
        cipherFilename = raw_input('Enter the filename for the ciphertext: ')
        try:
            cipherFilename = str(cipherFilename)
        except:
            cipherFilename = None
    if args.crack:
        cfile = open(cipherFilename, 'r')
        for line in cfile.readlines():
            cipherText = cipherText + line
        cfile.close()
        # Brute-force method. Try all 256 keys until one produces English text.
        possibles = []
        for i in range(0, WRAP+1):
            possible = encrypt_caesar(cipherText, i)
            possibles.append(possible)
            if get_fitness(possible) >= 0.30:
                print 'Key: '+str(i)+' Fitness: '+str(get_fitness(possible))+\
                      '\n  ' + possible
        return
    if args.plaintext != None:
        pfile = open(args.plaintext, 'r')
        for line in pfile.readlines():
            plainText = plainText + line
        pfile.close()
    else:
        plainText = raw_input('Please enter some plaintext: ')
    key = abs(args.key)
    while key > WRAP or key < 0:
        if key < 0:
            key = WRAP-abs(args.key)
        if key > WRAP:
            key = key-WRAP
    print 'Actual key is: '+str(key)
    cipherText = encrypt_caesar(plainText, key)
    cfile = open(cipherFilename, 'w')
    cfile.write(cipherText + '\n')
    cfile.close()
    print cipherText
    return

if __name__ == '__main__':
    main()
