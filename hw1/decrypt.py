#!/bin/python
from optparse import OptionParser
import random
letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
mapping = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"

def dec_letter(enc_letter):

    if enc_letter == " ":
        return enc_letter
    if enc_letter == "*":
        return enc_letter
    for i in range(0, len(mapping)):
        if enc_letter == mapping[i]:
            return letters[i]

def decrypt(encrypted_text):
    message = ""
    i = 3
    while i < len(encrypted_text):
        message = message + dec_letter(encrypted_text[i])
        i = i + 4
        
    return message

def main():

    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")
    (options, args) = parser.parse_args()
    
    filename = options.filename
    enc = open(filename, 'r')
    
    message = ""
    for line in enc:
        line = line.rstrip()
        message = message + " " + line + "*"
    message = message.lstrip()
    message = decrypt(message)
    
    newfilename = "decrypted_" + filename
    decrypted = open(newfilename, 'w')

    for i in range(0,len(message)):
        if message[i] == "*":
            decrypted.write('\n')
        else:
            decrypted.write(message[i])
    decrypted.close()

#    print(message)

if __name__ == '__main__':
    main()

    
