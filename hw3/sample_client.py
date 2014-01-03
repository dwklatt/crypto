# Echo client program
import socket

HOST = ''                       #Local Host
RemoteHOST = '128.153.188.7'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RemoteHOST, PORT))

def send_message(message):
    
    s.sendall('Hello, world')
    data = s.recv(1024)
    s.close()
    print 'Received', repr(data)
