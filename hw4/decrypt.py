def pulverizer(a, b, q, x1, y1, x2, y2):
    newx1 = x2
    #print(newx1)
    newy1 = y2
    #print(newy1)
    x2 = x1 - q*x2
    #print("x2 is: " + str(x2))
    y2 = y1 - q*y2
    #print("y2 is: " +str(y2))
    
    if b == 1:
        return y2

    q = int(a/b)
    #print(q)
    #a = q*b + r
    r = a - q*b
    if r == 0:
        #print(y2)
        return y2
    #print(r)
    
    return pulverizer(b, r, q, newx1, newy1, x2, y2)

def same_point_addition(h, p, A):
    x = long(h[0])
    y = long(h[1])
    topm = (3 * (x**2) + A) % p
    botm = (2 * y)
    botm = pulverizer(p,botm, 0, 0, 1, 0, 0)
    botm = botm % p
    m = (topm * botm) % p
    x3 = ((m ** 2) - 2*x) % p
    y3 = -(y + m*(x3 - x)) % p
    new_point = []
    new_point.append(x3)
    new_point.append(y3)
    return new_point

def point_addition(h1, h2, p):
    x1 = long(h1[0])
    y1 = long(h1[1])
    x2 = long(h2[0])
    y2 = long(h2[1])
    topm = (y2 - y1)
#    print(topm)
    botm = (x2 - x1) % p
    botm = pulverizer(p, botm, 0, 0, 1, 0, 0)
    botm = botm % p
#    print(botm)
    m = (topm * botm) % p
    x3 = ((m ** 2) - (x1 + x2)) % p
    y3 = -(y1 + m*(x3 - x1)) % p
    new_point = []
    new_point.append(x3)
    new_point.append(y3)
    return new_point

def point_mult(x, N, p, A):
    if N==1:
        return x
    elif N%2==0:
        x = same_point_addition(x,p,A)
        N = N/2
        return point_mult(x, N, p, A)
    else:
        y = same_point_addition(x,p,A)
        N = (N-1)/2
        return point_addition(x,point_mult(y,N,p, A),p)

def compute_full_mask(half_mask, N, p, A):
    #full_mask = half_mask
    #i = 0
    #while i < N:
    #    full_mask = point_addition(full_mask, half_mask, p)
    #    i = i + 1

    return point_mult(half_mask, N, p, A)

def compute_message(cipher, full_mask, p):
    full_mask[1] = -full_mask[1] % p
    message = point_addition(cipher, full_mask, p)
    message[1] = -message[1] % p
    return message

def decrypt(N, p, A):
    decrypted_message = ""
    half_mask = []
    cipher = []
    f = open('encrypted.txt', 'r+')
    for line in f:
        characters = line.split(" ")
        half_mask.append(characters[2])
        half_mask.append(characters[3])
#        print(half_mask)
        full_mask = compute_full_mask(half_mask, N, p, A)
        cipher.append(characters[0])
        cipher.append(characters[1])
        decrypted_message = decrypted_message + str(unichr(compute_message(cipher, full_mask, p)[0]))
        half_mask = []
        cipher = []
    f.close()
    return decrypted_message
    

def main():
    N = 182755680224874988969105090392374859247
    p = 231980187997634794246138521723892165531
    A = 286458106491124997002528249079664631375
#    print (p)
    answer = decrypt(N, p, A)
    print(answer)

#    H =[32,32]
#    C = [12,2]
#    test = point_mult(H,4,43,4)
#    print(test)
#    test[1] = -test[1] % 43
#    print(test)
#    hi = point_addition(C, test, 43) 
#    print("hi is: " + str(hi))


if __name__ == '__main__':
    main()
