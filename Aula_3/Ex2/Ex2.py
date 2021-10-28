#!/usr/bin/env python3

def addComplex(x, y):
    # add code here ...
    soma_real = x[0] + y[0]
    soma_imaginaria = x[1] + y[1]
    result=(soma_real, soma_imaginaria)
    return result

def multiplyComplex(x, y):
    # add code here ...
    Firsts=x[0]*y[0]
    Outers=x[0]+y[1]
    Inners=x[1]+y[0]
    Lasts= x[1]+y[1]

    soma_real = Firsts + Lasts *(-1)
    soma_imaginaria = Outers + Inners

    result=(soma_real, soma_imaginaria)
    return result

def printComplex(x):
    # add code here ...
    print(' O resultado é ' + str(x[0]) + '+' +str(x[1]) + 'i')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()