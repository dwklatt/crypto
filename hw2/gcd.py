#!/bin/python

def GCD(a, b):
    if b > 0:
        return GCD(b, a%b)

    return a

def main():
    fileE = open('e.txt', 'r')
    fileN = open('n.txt', 'r')
    e = fileE.readline()
    n = fileN.readline()
    fileE.close()
    fileN.close()
    e = long(e)
    n = long(n)
    d = GCD(n,e)
    fileD = open('d.txt','w')
    fileD.write(str(d))
if __name__ == '__main__':
    main()
