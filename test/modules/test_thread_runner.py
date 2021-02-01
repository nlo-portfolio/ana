#!/usr/bin/env python

import os
import unittest
import yaml

from modules import file_worker
from modules import thread_runner


class TestTAPRunner(unittest.TestCase):

    def setUp(self):
        self.append_str = 'augmented'
        self.input_filename = 'test_sample_file'
        self.output_filename = file_worker.append_str(self.input_filename, self.append_str)
        self.config = None
        with open('config.yml', 'r') as stream:
            self.config = yaml.safe_load(stream)['settings']

        self.input_filename = 'test_sample_file'
        with open(self.input_filename, 'w+') as input_file:
            input_file.write('alpha\nnumeric\naugmenter\n')

    def tearDown(self):
        try:
            os.remove(self.input_filename)
            os.remove(self.output_filename)
        except FileNotFoundError as e:
            pass

    def test_tap_runner_pass(self):
        write_queue_out = thread_runner.start(self.config, self.input_filename)
        self.assertEqual(write_queue_out.get(), ('alpha\n', '4lpha\n', 'a1pha\n', 'alph4\n', '41pha\n', '4lph4\n', 'a1ph4\n', '41ph4\n'))
        self.assertEqual(write_queue_out.get(), ('numeric\n', 'num3ric\n', 'numer1c\n', 'num3r1c\n'))
        self.assertEqual(write_queue_out.get(), ('augmenter\n', '4ugmenter\n', 'au6menter\n', 'augm3nter\n', 'augment3r\n', '4u6menter\n',
                                                 '4ugm3nter\n', '4ugment3r\n', 'au6m3nter\n', 'au6ment3r\n', 'augm3nt3r\n', '4u6m3nter\n',
                                                 '4u6ment3r\n', '4ugm3nt3r\n', 'au6m3nt3r\n', '4u6m3nt3r\n'))
        self.assertEqual(write_queue_out.get(), None)


if __name__ == '__main__':
    unittest.main(buffer=True)
