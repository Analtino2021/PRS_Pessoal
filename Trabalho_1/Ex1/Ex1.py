#!/usr/bin/env python3
from colorama import Fore, Back, Style
from time import time, ctime

def tic():
    # add code here ...
    return  time()

def toc():
    # add code here ...
    return time()

def main():
    # ex2 a)
    # a=tic()
    # print('This is ' + Fore.RED +'Ex1' + Style.RESET_ALL + ' and the current dat is '+ Fore.YELLOW +str(ctime()+ Style.RESET_ALL ))
    # b=toc()
    # print('Ellapsed time ' +str(b-a) + ' seconds .')

    # ex2 a)
    a=tic()
    print('This is ' + Fore.RED + 'Ex1' + Style.RESET_ALL + ' and the current dat is ' + Fore.YELLOW + str(ctime() + Style.RESET_ALL))
    x=[i for i in range(1, 50000000)]
    b=toc()
    print('Ellapsed time ' +str(b-a) + ' seconds .')


if __name__ == '__main__':
    main()