#!/usr/bin/env python

from sys import exit
from time import sleep


def append_str(filename, append_name):
    '''
    Appends a string to the filename to differentiate it from
    the original.
    
    Parameters:
        filename     (str):  the base filename.
        append_name  (str):  the string to append.
    
    Returns:
        str: the new filename with appendage.
    '''
    
    # Block added to support files with no extension.
    new_filename = ''
    if filename.rfind('.') > 0:
        new_filename = ''.join([filename[:filename.rfind('.')],
                                 '_', append_name, '.txt'])
    else:
        new_filename = ''.join([filename, '_', append_name, '.txt'])
    return new_filename

def read(filename, read_queue_out):
    '''
    Reads the original words from file.
    
    Parameters:
        filename        (str):          wordlist filename.
        read_queue_out  (queue.Queue):  queue out with words from wordlist.
    '''
    try:
        with open(filename) as input_file:
            for line_num, line_data in enumerate(input_file, 1):
                read_queue_out.put(line_data)
        read_queue_out.put(None)
    except OSError as e:
        print('File inaccessible. Exiting.')
        exit(1)

def write(filename, write_queue_in, write_queue_out):
    '''
    Writes the augmented words to file.
    
    Parameters:
        filename         (str):           filename to write.
        write_queue_in   (queue.Queue):   words to be written.
        write_queue_out  (queue.Queue):   words completed (for tally).
    '''
    new_filename = append_str(filename, 'augmented')
    output_file = open(new_filename, 'w')
    current_line = 1
    while True:
        augmented_list = write_queue_in.get()
        if augmented_list:
            for item in augmented_list:
                output_file.write(str(item))
            output_file.flush()
            write_queue_out.put(augmented_list)
            current_line += 1
        else:
            write_queue_out.put(None)
            break
    output_file.close()
