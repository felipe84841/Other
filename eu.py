#-------------------------------------------------------------------------------
# Name:        Euclidean algorithm
# Purpose:
#         Greatest common divisor
#
# Author:      Felipe Desiglo
#
# Created:     04/10/2016
# Copyright:   (c) Desiglo 2016
#-------------------------------------------------------------------------------

def gcd(a, b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a

def main():
    print gcd(1,2)
    print gcd(7,3)
    print gcd(5,25)
    print gcd(9,3)
    print gcd(100,104)
    pass

if __name__ == '__main__':
    main()
