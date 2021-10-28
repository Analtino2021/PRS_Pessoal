#!/usr/bin/env python3
from colorama import Fore, Back, Style
from pprint import pprint
from time import time, ctime
from colorama import Fore, Back, Style
from collections import namedtuple
import argparse
import readchar
import random

maximum_number = 10

def tic():
    # add code here ...
    return  time()

def toc():
    # add code here ...
    return time()

def right_letter(stop_key):

    # Ask for all the entries and put them in a list
    pressed_keys = []  # empty list to start with
    requested = []
    received = []
    duration = []
    inputs = []
    Total_inputs = {}
    accuracy = 0
    number_of_hits = 0
    number_of_types = 0
    while True:
        test_start = ctime()
        key_to_press = chr(random.randint(ord('a'), ord('z')))
        inicio=tic()
        print('Type letter '+ Fore.BLUE + str (key_to_press)+ Style.RESET_ALL )
        pressed_key = readchar.readkey()
        requested.append(key_to_press)

        if pressed_key == key_to_press:
            print('You typed  ' + Fore.GREEN + Style.BRIGHT + pressed_key + Style.RESET_ALL)
            fim=toc()
            test_end = ctime()
            number_of_hits += 1
            number_of_types += 1
            received.append(pressed_key)
            duration.append(fim-inicio)

            inputs = namedtuple('inputs', 'requested received duration')

           # print  'Type of Person:', type(Person)
            bob = inputs(str(key_to_press), str(pressed_key), str(fim-inicio))

          #  bob = Person(name='Bob', age=30, gender='male')
          #  print  '\nRepresentation:', bob
        else:
            print('You typed ' + Fore.RED + Style.BRIGHT + pressed_key + Style.RESET_ALL )
            fim = toc()
            test_end = ctime()
            number_of_types += 1
            pressed_keys.append(pressed_key)
            pressed_keys.append(pressed_key)
            received.append(pressed_key)
            duration.append(fim - inicio)
            # inputs.append('requested =' + str(key_to_press), 'received =' + str(pressed_key), 'duration =' + str(fim - inicio))

        if pressed_key == stop_key:
            print('You typed  ' + Fore.GREEN + Style.BRIGHT + pressed_key + Style.RESET_ALL + ' Terminatiing. ')
            break
        #inputs.append({'requested': requested,'received': received,'duration':duration})

        if maximum_number == number_of_types:
            print('Maximun Number achieved  ' + Fore.GREEN + Style.BRIGHT + str(number_of_types) + Style.RESET_ALL + ' Terminatiing. ')
            break

    # Analyse the list and count
    test_duration = 0
    count_wrong_typed_letters = 0
    count_right_typed_letters = 0
    pressed_numbers =[]
    pressed_others=[]

    Dic_pressed_others = {}

    for x in range(len(duration)):
        test_duration += duration[x]

        if str.isnumeric(pressed_key):
            count_wrong_typed_letters += 1
            pressed_numbers.append(pressed_key)

        else:
            count_right_typed_letters+= 1
            # pressed_others.append(pressed_key)
            # Dic_pressed_others.update({pressed_keys.index(pressed_key):pressed_key})

    type_average_duration = test_duration/maximum_number
    Total_inputs.update({'accuracy': accuracy, 'inputs': inputs,
    'number_of_hits': number_of_hits,
    'number_of_types': number_of_types,
     'test_duration': test_duration,
    'test_end': test_end,
    'test_start': test_start,
    'type_average_duration': type_average_duration,
    # 'type_hit_average_duration': type_hit_average_duration,
    # 'type_miss_average_duration': type_miss_average_duration
    })
    print(str(bob))
    pprint('Duration: ' + str(Total_inputs))

def main():
    ap= argparse.ArgumentParser(description='Process some integers.')
    ap.add_argument('-mn', '--max_number', type=int, required=True, help = 'Max number of secs fot Time mode or maximun number of inputs for number of imputs mode  .')
    # ap.add_argument('-mi', '--max_imputs', type=int, required=True, help = 'Max imputs to evaluete with right_letter.')

    args = vars(ap.parse_args())
    print(args)
    maximum_number = args['max_number']
    print(Fore.RED +'PSR ' + Style.RESET_ALL + 'Typing Test Analtino Martinho October 2021')
    right_letter('X')


if __name__ == '__main__':
    main()