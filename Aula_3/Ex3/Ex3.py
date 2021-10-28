#!/usr/bin/env python3
from collections import namedtuple

Complex = namedtuple('Complex',['r','i'])

def addComplex(x, y):
    # add code here ...
    soma_real = x.r + y.r
    soma_imaginaria = x.i + y.i
    result=Complex(r=soma_real, i=soma_imaginaria)
    return result

def multiplyComplex(x, y):
    # add code here ...
    Firsts=x.r*y.r
    Outers=x.r+y.i
    Inners=x.i+y.r
    Lasts= x.i+y.i

    soma_real = Firsts + Lasts *(-1)
    soma_imaginaria = Outers + Inners

    result=Complex(r=soma_real, i=soma_imaginaria)
    return result

def printComplex(x):
    # add code here ...
    print(' O resultado é ' + str(x.r) + '+' +str(x.i) + 'i')

def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

    # Test add
    c3=addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()