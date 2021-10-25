#!/usr/bin/env python3
from collections import namedtuple
'''
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

'''
class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def multiply(self, y):
        # addapt code to use classes
        Firsts = self.r * y.r
        Outers = self.r + y.i
        Inners = self.i + y.r
        Lasts = self.i + y.i

        soma_real = Firsts + Lasts * (-1)
        soma_imaginaria = Outers + Inners

        self = Complex(r=soma_real, i=soma_imaginaria)
        return self

    def add(self, y):
        # addapt code to use classes
        soma_real = self.r + y.r
        soma_imaginaria = self.i + y.i
        self = Complex(r=soma_real, i=soma_imaginaria)
        return self

    def __str__(self):

        return '(%g + %g''i)' % (self.r, self.i)


# addapt code to use classes

def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c2.add(c1)
    print(c2)  # uses the __str__ method in the class

if __name__ == '__main__':
    main()