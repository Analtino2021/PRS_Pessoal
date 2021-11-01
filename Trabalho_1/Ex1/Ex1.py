#!/usr/bin/env python3


from colorama import Fore, Back, Style, init
from time import time, ctime
from collections import namedtuple
from pprint import pprint
import argparse
import readchar
import random
import json
import string

maximum_number = 5


def tic():
    return time()


def toc():
    return time()


def right_letter(stop_key):
    pressed_keys = []
    requested = []
    received = []
    duration = []
    miss_duration = []
    hit_duration = []
    inputs_1 = []
    total_inputs = {}
    number_of_hits = 0
    number_of_types = 0

    while True:
        test_start = ctime()
        key_to_press = chr(random.randint(ord('a'), ord('z')))
        inicio = tic()

        print('Type letter ' + Fore.BLUE + str(key_to_press) + Style.RESET_ALL)

        pressed_key = readchar.readchar()
        requested.append(key_to_press)
        inputs = namedtuple('inputs', 'requested received duration')

        if pressed_key == key_to_press:
            print('You typed ' + Fore.GREEN + Style.BRIGHT + pressed_key + Style.RESET_ALL)
            fim = toc()
            test_end = ctime()
            number_of_hits += 1
            number_of_types += 1
            received.append(pressed_key)
            duration.append(fim - inicio)
            hit_duration.append(fim - inicio)

            bob = inputs(str(key_to_press), str(pressed_key), str(fim - inicio))
            inputs_1.append(bob)

        else:
            print('You typed ' + Fore.RED + Style.BRIGHT + pressed_key + Style.RESET_ALL)
            fim = toc()
            test_end = ctime()
            number_of_types += 1
            # pressed_keys.append(pressed_key)
            pressed_keys.append(pressed_key)
            received.append(pressed_key)
            duration.append(fim - inicio)

            bob = inputs(str(key_to_press), str(pressed_key), str(fim - inicio))
            inputs_1.append(bob)

        if pressed_key == stop_key:
            print('You typed ' + Fore.GREEN + Style.BRIGHT + pressed_key + Style.RESET_ALL + ' Terminating.')
            break

        if maximum_number == number_of_types:
            print('Maximum Number achieved ' + Fore.GREEN + Style.BRIGHT + str(
                number_of_types) + Style.RESET_ALL + ' Terminating.')
            break

    # Analysing the list and count
    test_total_duration = 0
    test_hit_duration = 0
    test_miss_duration = 0

    for x in range(len(duration)):
        test_total_duration += duration[x]

    for x in range(len(hit_duration)):
        test_hit_duration += hit_duration[x]

    for x in range(len(miss_duration)):
        test_miss_duration += miss_duration[x]

    accuracy = (number_of_hits / number_of_types) * 100
    type_average_duration = test_total_duration / maximum_number

    if number_of_hits == 0:
        type_hit_average_duration = 0
    else:
        type_hit_average_duration = test_hit_duration / number_of_hits

    if (number_of_types - number_of_hits) == 0:
        type_miss_average_duration = 0
    else:
        type_miss_average_duration = test_miss_duration / (number_of_types - number_of_hits)

    total_inputs.update({'accuracy': accuracy, 'inputs': inputs_1,
                         'number_of_hits': number_of_hits,
                         'number_of_types': number_of_types,
                         'test_duration': test_total_duration,
                         'test_end': test_end,
                         'test_start': test_start,
                         'type_average_duration': type_average_duration,
                         'type_hit_average_duration': type_hit_average_duration,
                         'type_miss_average_duration': type_miss_average_duration

                         })

    # pprint(json.dumps(total_inputs, sort_keys = True, indent = 2))
    # p = pprint(total_inputs)
    pprint(total_inputs)
    # print(p)


def main():
    ap = argparse.ArgumentParser(description='Process some integer.')
    ap.add_argument('-mn', '--maximun_number', type=int, help=' or maximum number of inputs for number of inputs mode')
    # ap.add_argument('-utm', '--use_time_mode', type=int, required=True ,help = ' maximum number of secs for Time mode')

    args = vars(ap.parse_args())
    print(args)

    maximum_number = args['maximun_number']
    print(Fore.RED + 'PSR ' + Style.RESET_ALL + ' Typing test')
    right_letter('X')


if __name__ == '__main__':
    main()