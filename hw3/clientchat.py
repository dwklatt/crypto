import os, socket, sys
import pp
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA
from Crypto.Cipher import AES

CLIENTHOST = ''
HOST = ''
PORT = 50007
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

ppservers = ()
job_server = pp.Server(ppservers=ppservers)
print "Starting pp with", job_server.get_ncpus(), "workers"

def talk():
    print 'to send a message hit CTRL-D'
    message = ""
    for line in sys.stdin:
        if 'quit()' in line:
            print 'exiting'
            return message
        message = message + line

def listen():
    while 1:
        data = client.recv(1024)
        if not data: break
        return data

def chat():
    while 1:
        message = talk()
        if 'quit()' in message:
            return
        client.sendall(message)
        print listen()

def main():
    print 'to quit type quit()'
#    job1 = job_server.submit(chat,(),(talk,listen),("socket",))
#    job1 = job_server.submit(talk)
#    job2 = job_server.submit(listen)
    chat()

if __name__ == '__main__':
    main()
