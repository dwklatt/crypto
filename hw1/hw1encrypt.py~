#!/bin/python
from optparse import OptionParser
import random
letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
mapping = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"

def map_letter(letter):
    
    if letter == " ":
        return letter
    for i in range(0, len(letters)):
        if letter == letters[i]:
            return mapping[i]

#    return letter

def encrypt(text):
    encrypted_message = ""
    for i in range(0,len(text)):
        encrypted_message = encrypted_message + mapping[random.randint(1,len(mapping)) - 1]
        encrypted_message = encrypted_message + mapping[random.randint(0,len(mapping)) - 1]
        encrypted_message = encrypted_message + mapping[random.randint(0,len(mapping)) - 1]
        encrypted_message = encrypted_message + map_letter(text[i])
    return encrypted_message

def dec_letter(enc_letter):

    if enc_letter == " ":
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
    message = open(filename, 'r')
    
    enc = ""
    for line in message:
        line = line.rstrip()
        enc = enc + " " + line
    enc = enc.lstrip()
    enc = encrypt(enc)
    print(enc)
    dec = decrypt(enc)
    print(dec)


if __name__ == '__main__':
    main()

    
