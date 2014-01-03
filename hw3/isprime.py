import random
import math
def special_pow(a,b,m):
    if b== 0:
        return 1
    elif b%2 == 0:
        y = special_pow(a,b/2,m)
        z = pow(a,b/2,m)
        if z == 1 and y!=1 and y!=m-1:
            return 0
        else:
            return z
    else:
        y = special_pow(a,b-1,m)
        z = pow(a*y, 1, m)
        return z

def is_prime(m, confidence):
    while confidence > 0:
        a = random.randrange(1, m-1)
        if(special_pow(a,m,m) != a):
            return False
        confidence = confidence - 1
    return True

def factors(a):
    factors = []
    i = 1
    j = a/4
    if j % 2 == 0:
        j = j + 1
    while i < a/4 and j < a/2:
        if a % i == 0:
            print ("FOUND ONE: " + str(i))
            factors.append(i)
        if a % j == 0:
            print ("FOUND ONE:" + str(j))
            factors.append(j)
        i = i + 2
        j = j + 2
        #print(i)
    return factors

def main():
    #print(is_prime(102112374625719848836417645466897582644268266380360636462856219195606277562091, 1000))
    a = 102112374625719848836417645466897582644268266380360636462856219195606277562091
    b = a
    #a = a/577
    #a = a/1231
    #a = a/4326083
    print(is_prime(33231478372611412280043463128457278882928121854454592410807842871,1000))
    #print b/a
    stuff = []
    stuff = factors(33231478372611412280043463128457278882928121854454592410807842871)
    print(stuff)
    

if __name__ == '__main__':
    main()
