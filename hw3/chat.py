import os, socket, sys
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA
from Crypto.Cipher import AES

HOST = ''
PORT = 50007
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
conn, addr = server.accept()

def talk():
    print 'to send a message hit CTRL-D'
    for line in sys.stdin:
        if 'quit()' in line:
            print 'exiting'
            return
        conn.sendall(line)

def listen():
    while 1:
        data = conn.recv(1024)
        if not data: break
        print data

def main():
    print 'to quit type quit()'
    talk()
    listen()
    

if __name__ == '__main__':
    main()
