import math
from Crypto import *

def pulverizer(a, b, q, x1, y1, x2, y2):
    newx1 = x2
    newy1 = y2
    x2 = x1 - q*x2
    y2 = y1 - q*y2
    if b == 1:
        return y2

    q = int(a/b)
    r = a - q*b
    if r == 0:
        return y2
    
    return pulverizer(b, r, q, newx1, newy1, x2, y2)

def decrypt_message(cipher,p,g,a,b):
    x = int(cipher[0])
#    print(x)
#    a = a / 577
#    x = pow(x,577) % p
#    print(x)
#    a = a / 1231
#    x = pow(x,1231) % p
#    print(x)
#    a = a / 4326083
#    x = pow(x,4326083) % p
#    print(x)
    x = pow(x,a,p)
#    print(x)
    y = int(cipher[1])
#    print(y)
    x = pulverizer(p,x,0,0,1,0,0) % p
#    x = inverse(x,p)
    return (x * y) % p

def decrypt(p,g,a,b):
    f = open('encrypted.txt', 'r+')
    message = ""
    for line in f:
        cipher = line.split(",")
        message = message + str(unichr(decrypt_message(cipher,p,g,a,b)))
    
    f.close()
    return message

def main():
    p = 211287523889848166456771978073530465593093161450010064509303400255860514422619
    g = 15944282073914562075116370489962003433567850159612874030242082495627173757989
    a = 102112374625719848836417645466897582644268266380360636462856219195606277562091
    b = 99875420304905788162304238315680480125682219886353666515441718590579015480458

    message = decrypt(p,g,a,b)
    print(message)

if __name__ == '__main__':
    main()
