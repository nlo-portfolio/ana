#!/usr/bin/env python

from classes import permutation_engine


def augment(config, read_queue_out, write_queue_in):
    '''
    Augments the wordlist by generating permutations for each word from
    the queue.
    
    Parameters:
        config          (dict):         config file as a dictionary.
        read_queue_out  (queue.Queue):  queue containing original words.
        write_queue_in  (queue.Queue):  queue containing permutated words.
    '''
    engine = permutation_engine.PermutationEngine(config)
    while True:
        new_word = read_queue_out.get()
        if new_word:
            line_list = engine.permutate(new_word)
            write_queue_in.put(line_list)
        else:
            write_queue_in.put(None)
            break
