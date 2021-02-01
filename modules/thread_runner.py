#!/usr/bin/env python

import threading
from queue import Queue

from classes import permutation_engine
from modules import augment_worker
from modules import file_worker


def start(config, input_filename):
    '''
    Starts all threads.
    
    Parameters:
        cpu_count       (int):   number of cpus.
        config          (dict):  config file as a dictionary.
        input_filename  (str):   string name for the input file.
    
    Returns:
        queue.Queue: the end queue with all processed items.
    '''
    read_queue_out = Queue()
    write_queue_in = Queue()
    write_queue_out = Queue()

    read_thread = threading.Thread(target=file_worker.read, args=(input_filename, read_queue_out,), daemon=True)
    write_thread = threading.Thread(target=file_worker.write, args=(input_filename, write_queue_in, write_queue_out,), daemon=True)
    augment_thread = threading.Thread(target=augment_worker.augment, args=(config, read_queue_out, write_queue_in), daemon=True)

    read_thread.start()
    write_thread.start()
    augment_thread.start()

    return write_queue_out
