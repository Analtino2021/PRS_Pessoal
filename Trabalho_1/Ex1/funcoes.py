#!/usr/bin/env python3
import json

from colorama import Fore, Back, Style
from pprint import pprint
from time import time, ctime
from colorama import Fore, Back, Style
from collections import namedtuple
import argparse
import readchar
import random

maximum_number = 5

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
    miss_duration=[]
    hit_duration = []
    inputs_1 = []
    Total_inputs = {}
    number_of_hits = 0
    number_of_types = 0
    while True:
        test_start = ctime()
        key_to_press = chr(random.randint(ord('a'), ord('z')))
        inicio=tic()
        print('Type letter '+ Fore.BLUE + str(key_to_press)+ Style.RESET_ALL )
        pressed_key = readchar.readkey()
        requested.append(key_to_press)
        inputs = namedtuple('inputs', 'requested received duration')

        if pressed_key == key_to_press:
            print('You typed  ' + Fore.GREEN + Style.BRIGHT + pressed_key + Style.RESET_ALL)
            fim=toc()
            test_end = ctime()
            number_of_hits += 1
            number_of_types += 1
            received.append(pressed_key)
            duration.append(fim-inicio)
            hit_duration.append(fim-inicio)

            bob = inputs(str(key_to_press), str(pressed_key), str(fim-inicio))
            inputs_1.append(bob)

        else:
            print('You typed ' + Fore.RED + Style.BRIGHT + pressed_key + Style.RESET_ALL )
            fim = toc()
            test_end = ctime()
            number_of_types += 1
            # pressed_keys.append(pressed_key)
            pressed_keys.append(pressed_key)
            received.append(pressed_key)
            duration.append(fim - inicio)
            miss_duration.append(fim - inicio)

            bob = inputs(str(key_to_press), str(pressed_key), str(fim - inicio))
            inputs_1.append(bob)

        if pressed_key == stop_key:
            print('You typed  ' + Fore.GREEN + Style.BRIGHT + pressed_key + Style.RESET_ALL + ' Terminating. ')
            break

        if maximum_number == number_of_types:
            print('Maximun Number achieved  ' + Fore.GREEN + Style.BRIGHT + str(number_of_types) + Style.RESET_ALL
                  + ' Terminating. ')
            break

    # Analyse the list and count
    test_total_duration  = 0
    test_hit_duration = 0
    test_miss_duration = 0

    for x in range(len(duration)):
        test_total_duration += duration[x]

    for x in range(len(hit_duration)):
        test_hit_duration += hit_duration[x]

    for x in range(len(miss_duration)):
        test_miss_duration += miss_duration[x]

    accuracy=(number_of_hits/number_of_types)*100

    type_average_duration = test_total_duration / maximum_number

    if number_of_hits == 0:
        type_hit_average_duration = 0
    else:
        type_hit_average_duration = test_hit_duration / number_of_hits

    if (number_of_types-number_of_hits) == 0:
        type_miss_average_duration = 0
    else:
        type_miss_average_duration = test_miss_duration / (number_of_types-number_of_hits)

    Total_inputs.update({'accuracy': accuracy, 'inputs': str(inputs_1),
    'number_of_hits': number_of_hits,
    'number_of_types': number_of_types,
    'test_duration': test_total_duration,
    'test_start': test_start,
    'test_end': test_end,
    'type_average_duration': type_average_duration,
    'type_hit_average_duration': type_hit_average_duration,
    'type_miss_average_duration': type_miss_average_duration
    })

    pprint(json.dumps(Total_inputs,sort_keys=False,indent=2))

def main():
    ap= argparse.ArgumentParser(description='Process some integers.')
    ap.add_argument('-mn', '--max_number', type=int, required=True, help = 'or maximun number of inputs for number of inputs mode  .')
    #ap.add_argument('-utm', '--use_time_mode',type=int, required=True, help = 'Max number of secs for Time mode.')
    args = vars(ap.parse_args())
    print(args)
    maximum_number = args['max_number']
    print(Fore.RED +'PSR ' + Style.RESET_ALL + 'Typing Test Analtino Martinho October 2021')
    right_letter('X')


if __name__ == '__main__':
    main()