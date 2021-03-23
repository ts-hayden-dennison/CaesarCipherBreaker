# reverse cipher by Hayden Dennison
# to decrypt pass in the ciphertext as plaintext
import argparse

def encrypt_reverse(plainText):
    cipherText = ''
    plainList = list(plainText)
    plainList.reverse()
    for char in plainList:
        cipherText = cipherText + char
    return cipherText

def get_parser():
    parser = argparse.ArgumentParser(\
                description='Encrypt a message in reverse cipher')
    parser.add_argument('-p', '--plaintext', type=str, action='store', \
                        help='The filename of the plaintext file.', \
                        default=None)
    parser.add_argument('-c', '--ciphertext', type=str, action='store', \
                        help='The filename of the ciphertext file.', \
                        default=None)
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    plainText = ''
    cipherText = ''
    cipherFilename = args.ciphertext
    if args.plaintext != None:
        pfile = open(args.plaintext, 'r')
        for line in pfile.readlines():
            plainText = plainText + line
        pfile.close()
    else:
        plainText = raw_input('Please enter some plaintext: ')
    while cipherFilename == None:
        cipherFilename = raw_input('Enter the filename for the ciphertext: ')
        try:
            cipherFilename = str(cipherFilename)
        except:
            cipherFilename = None
    cipherText = encrypt_reverse(plainText)
    cfile = open(cipherFilename, 'w')
    cfile.write(cipherText + '\n')
    cfile.close()
    print 'Ciphertext: ' + cipherText + '\n'
    return

if __name__ == '__main__':
    main()
