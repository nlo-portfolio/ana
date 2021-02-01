#!/usr/bin/env python

import sys
import copy
import itertools


class PermutationEngine(object):
    '''
    Class used for performing the permutations on a single word.
    
    Attributes:
        default_values        (list):  the alpha characters to be replaced.
        default_permutations  (list):  substitute values for the alpha characters.
        ppw                   (int):   permutations per word.
        pt                    (int):   permutations total for each word.
        include_original      (bool):  includes the original word in the new wordlist.
        start                 (int):   index to start at, supports including the original word.
    '''

    def __init__(self, config):
        '''
        Class constructor.
        
        Parameters:
            config  (dict):  the loaded configuration file.
        '''
        self.default_values = config['alpha_values']
        self.default_permutations = config['numerical_values']
        self.ppw = config['ppw']
        self.pt = config['pt']
        self.include_original = config['include_original']
        # Determine if original string will be included with the output permutations
        # First combination (index 0) is always zero substitutions
        self.start = 0 if self.include_original else 1
        # (+1) is to account for original string if selected
        self.ppw = self.ppw + 1 if self.include_original else self.ppw
        self.pt = self.pt + 1 if self.include_original else self.pt

    def create_index_list(self, input_str_list):
        '''
        Creates a list with the indexes to be replaced.
        
        Parameters:
            input_str_list  (list):  the input string as a list of characters.
        
        Returns:
            tuple: contains the index pairings for replacement.
        '''
        index_list_subs = []
        t_index_list_subs = []
        for i in range(len(input_str_list)):
            for j in range(len(self.default_values)):
                if input_str_list[i] is self.default_values[j]:
                    t_index_list_subs.append(i)
                    t_index_list_subs.append(self.default_permutations[j])
                    t_index_list_subs = tuple(t_index_list_subs)
                    index_list_subs.append(t_index_list_subs)
                    t_index_list_subs = []
        return tuple(index_list_subs)

    def create_permutation_list(self, index_list_subs):
        '''
        Creates all of the different possible permuatations of the input string.
        
        Parameters:
            index_list_subs  (list):  contains the indexes to be replaced.
        
        Returns:
            tuple: contains the different possible permutations for the input string.
        '''
        index_combinations = []
        index_combinations = tuple(c for i in range(self.ppw)
                                     for c in itertools.combinations(index_list_subs, i))
        return tuple(index_combinations)

    def replace_alpha_indices(self, input_str_list, index_combinations):
        '''
        Replaces the alpha indices with numeric substitutes.
        
        Parameters:
            intput_str_list     (list):  the input string as a list of characters.
            index_combinations  (list):  list of tuples containing the pairs of alpha and numeric characters.
        
        Returns:
            list: contains all of the new augmented strings for the input word.
        '''
        return_string = []
        return_string_list = []
        perms_current = 0
        for i in range(self.start, len(index_combinations)):
            if (perms_current == self.ppw) or (perms_current == self.pt):
                return tuple(return_string_list)
            return_string = list(input_str_list)
            for j in range(len(index_combinations[i])):
                return_string[index_combinations[i][j][0]] = index_combinations[i][j][1]
            return_string_list.append(''.join(return_string) + '\n')
            perms_current += 1
        return tuple(return_string_list)

    def permutate(self, input_string):
        '''
        Permutates a word given as an input string.
        
        Parameters:
            input_string  (str):  the input string to be permutated.
        
        Returns:
            list: contains all of the new augmented strings for the input word.
        '''
        input_str_list = list(input_string.rstrip('\n'))
        index_list_subs = self.create_index_list(input_str_list)
        index_combinations = self.create_permutation_list(index_list_subs)
        return self.replace_alpha_indices(input_str_list, index_combinations)
