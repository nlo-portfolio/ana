#!/usr/bin/env python

import unittest
import yaml

from classes import permutation_engine


class TestPermutationEngine(unittest.TestCase):

    def setUp(self):
        config = None
        with open('config.yml', 'r') as stream:
            config = yaml.safe_load(stream)['settings']
        self.pe = permutation_engine.PermutationEngine(config)
        self.index_combinations = ((), ((0, '4'),), ((2, '4'),), ((4, '3'),), ((6, '1'),), ((10, '3'),), ((11, '5'),), ((13, '3'),), ((0, '4'), (2, '4')), ((0, '4'), (4, '3')), ((0, '4'), (6, '1')), ((0, '4'), (10, '3')), ((0, '4'), (11, '5')), ((0, '4'), (13, '3')), ((2, '4'), (4, '3')), ((2, '4'), (6, '1')), ((2, '4'), (10, '3')), ((2, '4'), (11, '5')), ((2, '4'), (13, '3')), ((4, '3'), (6, '1')), ((4, '3'), (10, '3')), ((4, '3'), (11, '5')), ((4, '3'), (13, '3')), ((6, '1'), (10, '3')), ((6, '1'), (11, '5')), ((6, '1'), (13, '3')), ((10, '3'), (11, '5')), ((10, '3'), (13, '3')), ((11, '5'), (13, '3')), ((0, '4'), (2, '4'), (4, '3')), ((0, '4'), (2, '4'), (6, '1')), ((0, '4'), (2, '4'), (10, '3')), ((0, '4'), (2, '4'), (11, '5')), ((0, '4'), (2, '4'), (13, '3')), ((0, '4'), (4, '3'), (6, '1')), ((0, '4'), (4, '3'), (10, '3')), ((0, '4'), (4, '3'), (11, '5')), ((0, '4'), (4, '3'), (13, '3')), ((0, '4'), (6, '1'), (10, '3')), ((0, '4'), (6, '1'), (11, '5')), ((0, '4'), (6, '1'), (13, '3')), ((0, '4'), (10, '3'), (11, '5')), ((0, '4'), (10, '3'), (13, '3')), ((0, '4'), (11, '5'), (13, '3')), ((2, '4'), (4, '3'), (6, '1')), ((2, '4'), (4, '3'), (10, '3')), ((2, '4'), (4, '3'), (11, '5')), ((2, '4'), (4, '3'), (13, '3')), ((2, '4'), (6, '1'), (10, '3')), ((2, '4'), (6, '1'), (11, '5')), ((2, '4'), (6, '1'), (13, '3')), ((2, '4'), (10, '3'), (11, '5')), ((2, '4'), (10, '3'), (13, '3')), ((2, '4'), (11, '5'), (13, '3')), ((4, '3'), (6, '1'), (10, '3')), ((4, '3'), (6, '1'), (11, '5')), ((4, '3'), (6, '1'), (13, '3')), ((4, '3'), (10, '3'), (11, '5')), ((4, '3'), (10, '3'), (13, '3')), ((4, '3'), (11, '5'), (13, '3')), ((6, '1'), (10, '3'), (11, '5')), ((6, '1'), (10, '3'), (13, '3')), ((6, '1'), (11, '5'), (13, '3')), ((10, '3'), (11, '5'), (13, '3')), ((0, '4'), (2, '4'), (4, '3'), (6, '1')), ((0, '4'), (2, '4'), (4, '3'), (10, '3')), ((0, '4'), (2, '4'), (4, '3'), (11, '5')), ((0, '4'), (2, '4'), (4, '3'), (13, '3')), ((0, '4'), (2, '4'), (6, '1'), (10, '3')), ((0, '4'), (2, '4'), (6, '1'), (11, '5')), ((0, '4'), (2, '4'), (6, '1'), (13, '3')), ((0, '4'), (2, '4'), (10, '3'), (11, '5')), ((0, '4'), (2, '4'), (10, '3'), (13, '3')), ((0, '4'), (2, '4'), (11, '5'), (13, '3')), ((0, '4'), (4, '3'), (6, '1'), (10, '3')), ((0, '4'), (4, '3'), (6, '1'), (11, '5')), ((0, '4'), (4, '3'), (6, '1'), (13, '3')), ((0, '4'), (4, '3'), (10, '3'), (11, '5')), ((0, '4'), (4, '3'), (10, '3'), (13, '3')), ((0, '4'), (4, '3'), (11, '5'), (13, '3')), ((0, '4'), (6, '1'), (10, '3'), (11, '5')), ((0, '4'), (6, '1'), (10, '3'), (13, '3')), ((0, '4'), (6, '1'), (11, '5'), (13, '3')), ((0, '4'), (10, '3'), (11, '5'), (13, '3')), ((2, '4'), (4, '3'), (6, '1'), (10, '3')), ((2, '4'), (4, '3'), (6, '1'), (11, '5')), ((2, '4'), (4, '3'), (6, '1'), (13, '3')), ((2, '4'), (4, '3'), (10, '3'), (11, '5')), ((2, '4'), (4, '3'), (10, '3'), (13, '3')), ((2, '4'), (4, '3'), (11, '5'), (13, '3')), ((2, '4'), (6, '1'), (10, '3'), (11, '5')), ((2, '4'), (6, '1'), (10, '3'), (13, '3')), ((2, '4'), (6, '1'), (11, '5'), (13, '3')), ((2, '4'), (10, '3'), (11, '5'), (13, '3')), ((4, '3'), (6, '1'), (10, '3'), (11, '5')), ((4, '3'), (6, '1'), (10, '3'), (13, '3')), ((4, '3'), (6, '1'), (11, '5'), (13, '3')), ((4, '3'), (10, '3'), (11, '5'), (13, '3')), ((6, '1'), (10, '3'), (11, '5'), (13, '3')), ((0, '4'), (2, '4'), (4, '3'), (6, '1'), (10, '3')), ((0, '4'), (2, '4'), (4, '3'), (6, '1'), (11, '5')), ((0, '4'), (2, '4'), (4, '3'), (6, '1'), (13, '3')), ((0, '4'), (2, '4'), (4, '3'), (10, '3'), (11, '5')), ((0, '4'), (2, '4'), (4, '3'), (10, '3'), (13, '3')), ((0, '4'), (2, '4'), (4, '3'), (11, '5'), (13, '3')), ((0, '4'), (2, '4'), (6, '1'), (10, '3'), (11, '5')), ((0, '4'), (2, '4'), (6, '1'), (10, '3'), (13, '3')), ((0, '4'), (2, '4'), (6, '1'), (11, '5'), (13, '3')), ((0, '4'), (2, '4'), (10, '3'), (11, '5'), (13, '3')), ((0, '4'), (4, '3'), (6, '1'), (10, '3'), (11, '5')), ((0, '4'), (4, '3'), (6, '1'), (10, '3'), (13, '3')), ((0, '4'), (4, '3'), (6, '1'), (11, '5'), (13, '3')), ((0, '4'), (4, '3'), (10, '3'), (11, '5'), (13, '3')), ((0, '4'), (6, '1'), (10, '3'), (11, '5'), (13, '3')), ((2, '4'), (4, '3'), (6, '1'), (10, '3'), (11, '5')), ((2, '4'), (4, '3'), (6, '1'), (10, '3'), (13, '3')), ((2, '4'), (4, '3'), (6, '1'), (11, '5'), (13, '3')), ((2, '4'), (4, '3'), (10, '3'), (11, '5'), (13, '3')), ((2, '4'), (6, '1'), (10, '3'), (11, '5'), (13, '3')), ((4, '3'), (6, '1'), (10, '3'), (11, '5'), (13, '3')), ((0, '4'), (2, '4'), (4, '3'), (6, '1'), (10, '3'), (11, '5')), ((0, '4'), (2, '4'), (4, '3'), (6, '1'), (10, '3'), (13, '3')), ((0, '4'), (2, '4'), (4, '3'), (6, '1'), (11, '5'), (13, '3')), ((0, '4'), (2, '4'), (4, '3'), (10, '3'), (11, '5'), (13, '3')), ((0, '4'), (2, '4'), (6, '1'), (10, '3'), (11, '5'), (13, '3')), ((0, '4'), (4, '3'), (6, '1'), (10, '3'), (11, '5'), (13, '3')), ((2, '4'), (4, '3'), (6, '1'), (10, '3'), (11, '5'), (13, '3')), ((0, '4'), (2, '4'), (4, '3'), (6, '1'), (10, '3'), (11, '5'), (13, '3')))
        self.augmented_list = tuple((
            'academic tester\n', '4cademic tester\n', 'ac4demic tester\n', 'acad3mic tester\n',
            'academ1c tester\n', 'academic t3ster\n', 'academic te5ter\n', 'academic test3r\n',
            '4c4demic tester\n', '4cad3mic tester\n', '4cadem1c tester\n', '4cademic t3ster\n',
            '4cademic te5ter\n', '4cademic test3r\n', 'ac4d3mic tester\n', 'ac4dem1c tester\n',
            'ac4demic t3ster\n', 'ac4demic te5ter\n', 'ac4demic test3r\n', 'acad3m1c tester\n',
            'acad3mic t3ster\n'
        ))

    def tearDown(self):
        pass

    def test_create_index_list_pass(self):
        index_list_subs = self.pe.create_index_list(list('academic tester'))
        self.assertEqual(index_list_subs, ((0, '4'), (2, '4'), (4, '3'), (6, '1'), (10, '3'), (11, '5'), (13, '3')))

    def test_create_permutation_list_pass(self):
        index_combinations = self.pe.create_permutation_list(((0, '4'), (2, '4'), (4, '3'), (6, '1'), (10, '3'), (11, '5'), (13, '3')))
        self.assertEqual(index_combinations, self.index_combinations)

    def test_replace_alpha_indices_pass(self):
        augmented_list = self.pe.replace_alpha_indices(list('academic tester'), self.index_combinations)
        self.assertEqual(augmented_list, self.augmented_list)

    def test_permutate(self):
        return_value = self.pe.permutate('academic tester')
        self.assertEqual(return_value, self.augmented_list)


if __name__ == '__main__':
    unittest.main(buffer=True)
