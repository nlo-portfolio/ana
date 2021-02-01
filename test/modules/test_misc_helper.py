#!/usr/bin/env python

import io
import os
import unittest
import sys
from queue import Queue

from modules import misc_helper
from modules import file_worker


class TestMiscHelper(unittest.TestCase):

    def setUp(self):
        self.config_name = 'config.yml'
        self.append_str = 'augmented'
        self.input_filename = 'test_sample_file'
        self.output_filename = file_worker.append_str(self.input_filename, self.append_str)
        self.sample_truth = 'alpha\n4lpha\na1pha\nalph4\n41pha\n4lph4\na1ph4\n41ph4\nnumeric\nnum3ric\nnumer1c\nnum3r1c\naugmenter\n4ugmenter\nau6menter\naugm3nter\naugment3r\n4u6menter\n4ugm3nter\n4ugment3r\nau6m3nter\nau6ment3r\naugm3nt3r\n4u6m3nter\n4u6ment3r\n4ugm3nt3r\nau6m3nt3r\n4u6m3nt3r\n'
        with open(self.input_filename, 'w+') as input_file:
            input_file.write('alpha\nnumeric\naugmenter\n')

        # Capture stdout during test.
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

    def tearDown(self):
        try:
            os.remove(self.input_filename)
            os.remove(self.output_filename)
        except FileNotFoundError as e:
            pass

        # Re-enable stdout after test.
        sys.stdout = sys.__stdout__

    def test_generate_sample_file_pass(self):
        misc_helper.generate_sample_file(self.input_filename)
        sample_string = ''
        with open(self.output_filename, 'r') as sample_file:
            for line in sample_file:
                sample_string += line
        self.assertEqual(sample_string, self.sample_truth)

    def test_check_sample_file_pass(self):
        with open(self.output_filename, 'w+') as output_file:
            output_file.write(self.sample_truth)
        result = misc_helper.check_sample_file(self.input_filename)
        self.assertTrue(result)

    def test_check_sample_file_fail(self):
        with open(self.output_filename, 'a') as output_file:
            output_file.write('distort')
        result = misc_helper.check_sample_file(self.input_filename)
        self.assertFalse(result)

    def test_parse_config_pass(self):
        config = misc_helper.parse_config(self.config_name)
        self.assertTrue('alpha_values' in config)
        self.assertTrue('numerical_values' in config)

    def test_parse_config_fail(self):
        with self.assertRaises(FileNotFoundError) as cm:
            config = misc_helper.parse_config(self.config_name + 'error')


if __name__ == '__main__':
    unittest.main(buffer=False)
