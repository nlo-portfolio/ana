#!/usr/bin/env python

'''
This module provides some functions for requesting and validating input from the user.
Includes: request for the input wordlist filename, integers (for ppw and pt) and the
the string to append to the original filename for the new wordlist file.
'''

import os


def request_input_filename():
    '''
    Prompts the user to input the filename for the original wordlist. Will re-prompt if no such file exists.
    Will also output a sample file if the user inputs '--SAMPLE' (and then terminates).
    
    Parameters:
        None
    
    Returns:
        str: the filename of the input wordlist (or none if a sample is to be generated).
    '''
    filename = ''
    while not os.path.isfile(filename):
        print("Enter the filename of the wordlist to be augmented (cwd = '" +
              os.getcwd().rpartition(os.path.sep)[2] + "') [enter --sample to produce a sample augmented file]: ")
        filename = input()
        if filename.upper() == '--SAMPLE':
            return None
        if os.path.isfile(filename):
            break
        else:
            print('Invalid filename. Please try again.\n')
    return filename


def request_integer(message):
    '''
    Prompts the user to input a valid integer, and will re-prompt if invalid.
    
    Parameters:
        message  (str):  the message to be displayed at the prompt for the user.
    
    Returns:
        int: the input value from the user.
    '''
    print(message)
    while True:
        try:
            value = input()
            return int(value)
        except ValueError as e:
            if not value:
                print('Using default value.')
                return None
            print(message)


def request_include_original():
    '''
    Prompts the user to enter 'Y/N' to indicate if the original word should also be included in the new wordlist.
    
    Parameters:
        None
    
    Returns:
        bool: includes the original string if true, excludes it if false.
    '''
    user_input = '-1'
    include_original = True
    while ((user_input.upper() != 'Y') and
          (user_input.upper() != 'N') and
          (user_input != '')):
        print("Include original word? Enter 'Y'/'N' [default = 'Y']: ")
        user_input = input()
        if user_input.upper() == 'Y': include_original = True
        elif user_input.upper() == 'N': include_original = False
        else: print("Invalid input. Please enter either 'Y' or 'N' or (leave blank for default.)\n")
    if not user_input:
        print('Using default value.')
    return include_original
