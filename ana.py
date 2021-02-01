#!/usr/bin/env python

'''
Filename: ana.py
Author: nlo
Python Version: 3.8.5

ANA (Alpha Numeric Augmenter) is a tool to modify existing word lists,
by substituting numbers for letters, as is common for people to do when
attempting to strengthen their password. This program can be duplicated
in John the Ripper using the appropriate parameters. However, this program
is designed to output a completely new file with the augmented results.

Please see the configuraiton file for more information and usage.
'''

import datetime
import queue
import sys
import threading
from queue import Queue

from classes import permutation_engine
from modules import augment_worker
from modules import file_worker
from modules import input_helper
from modules import misc_helper
from modules import thread_runner


def main():
    '''
    Main driver for the program, requests input from the user and augments the provided wordlist.
    
    Parameters:
        None
    '''
    if len(sys.argv) == 2 and sys.argv[1] == '--sample':
        return misc_helper.generate_sample_file('ana_sample_input.txt')

    config = misc_helper.parse_config('config.yml')
    if not config:
        print('''There is an error with the 'config.yml' file. It may be missing or corrupted.''')
        sys.exit()

    input_filename = input_helper.request_input_filename()
    if not input_filename:
        return misc_helper.generate_sample_file('ana_sample')
    ppw = input_helper.request_integer('Please enter the permutations per word (ppw) [default {}]: '.format(config['ppw']))
    pt = input_helper.request_integer('Please enter the permutations total (pt) [default {}]: '.format(config['pt']))
    include_original = input_helper.request_include_original()

    if ppw: config['ppw'] = ppw
    if pt: config['pt'] = pt
    if include_original: config['include_original'] = include_original

    before = datetime.datetime.now()

    write_queue_out = thread_runner.start(config, input_filename)
    misc_helper.wait_for_completion(write_queue_out)

    after = datetime.datetime.now()
    delta = after - before
    print('Time Elapsed (seconds): {}'.format(delta.seconds))
    print('Process Complete.')


if __name__ == '__main__':
    # cProfile.run('main()')
    main()
