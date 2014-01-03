#!/bin/python
from optparse import OptionParser
import random
letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
mapping = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"

def map_letter(letter):
    
    if letter == " ":
        return letter
    if letter == "*":
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
        enc = enc + " " + line + "*"
    enc = enc.lstrip()

    newfilename = "encrypted_" + filename
    enc = encrypt(enc)
    encrypted = open(newfilename, 'w')
    print(len(enc))
    for i in range(0,len(enc)):
        if enc[i] == "*":
            encrypted.write('\n')
        else:
            encrypted.write(enc[i])
    encrypted.close()
#    print(enc)

if __name__ == '__main__':
    main()

    
