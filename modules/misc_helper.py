#!/usr/bin/env python

from queue import Queue
from yaml import safe_load, YAMLError

from classes import permutation_engine
from modules import file_worker
from modules import thread_runner


def wait_for_completion(write_queue_out, output=True):
    '''
    Waits for all processes and threads to complete and displays real-time progress.
    Reception of (None, None) signifies the process is complete.
    
    Parameters:
        write_queue_out  (queue.Queue):  the final output queue in the process.
    '''
    words_done = 0
    while True:
        permutation_list = write_queue_out.get()
        if (words_done % 50 == 0) and output:
            print("\r" + "{} words processed...".format(words_done), end='')

        if permutation_list:
            words_done += 1
            continue
        else:
            if output:
                print("\r" + "{} words processed...".format(words_done))
            break

def generate_sample_file(input_filename):
    '''
    Generates a new original wordlist and outputs the permutations for a sample.
    
    Parameters:
        None
    '''
    print('Generating sample...')
    try:
        input_file = open(input_filename, 'w+')
        input_file.write('alpha\nnumeric\naugmenter\n')
    except:
        print('Error creating sample input file')
    finally:
        input_file.close()
    config = parse_config('config.yml')
    if not config:
        print('''There is an error with the \'Configuration.ini\' file. It may be missing or corrupted.''')
        return False

    write_queue_out = thread_runner.start(config, input_filename)
    wait_for_completion(write_queue_out, False)
    print('Sample complete.')
    return check_sample_file(input_filename)


def check_sample_file(input_filename):
    '''
    Performs a validation check on the sample file for testing purposes.
    
    Parameters:
        None
    '''
    sample_string = ''
    sample_filename = file_worker.append_str(input_filename, 'augmented')
    with open(sample_filename, 'r') as sample_file:
        for line in sample_file:
            sample_string += line

    sample_check = 'alpha\n4lpha\na1pha\nalph4\n41pha\n4lph4\na1ph4\n41ph4\nnumeric\nnum3ric\nnumer1c\nnum3r1c\naugmenter\n4ugmenter\nau6menter\naugm3nter\naugment3r\n4u6menter\n4ugm3nter\n4ugment3r\nau6m3nter\nau6ment3r\naugm3nt3r\n4u6m3nter\n4u6ment3r\n4ugm3nt3r\nau6m3nt3r\n4u6m3nt3r\n'
    if sample_string == sample_check:
        print('Sample file check successful.')
        return True
    else:
        print('Sample file check failed')
        return False


def parse_config(filename):
    '''
    Opens and loads the yaml configuration file for reading and returns the configuration as a dictionary.
    
    Paramaters:
        filename  (str):  filename for the configuration file.
        
    Returns:
        dict: contains the keys and values for the configuration.
    '''
    with open(filename, 'r') as stream:
        try:
            return safe_load(stream)['settings']
        except YAMLError as e:
            print('Configuration file (config.yaml) is missing or corrupted. Exiting.')
