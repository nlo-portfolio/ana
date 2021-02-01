#!/usr/bin/env python

import io
import os
import sys
import unittest
from unittest.mock import patch

from modules import input_helper


class TestInputHelper(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('builtins.input', return_value=os.path.dirname(os.path.dirname(__file__)) + '/test_file')
    def test_request_input_filename_pass(self, return_value):
        # Capture stdout during test.
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        filename = input_helper.request_input_filename()
        self.assertEqual(filename, os.path.dirname(os.path.dirname(__file__)) + '/test_file')
        self.assertEqual(
            suppress_text.getvalue(), "Enter the filename of the wordlist to be augmented (cwd = '{}') [enter --sample to produce a sample augmented file]: \n".format(
                                      os.getcwd().rpartition(os.path.sep)[2])
        )
        # Re-enable stdout after test.
        sys.stdout = sys.__stdout__

    @patch('builtins.input', return_value='1')
    def test_request_integer_pass(self, return_value):
        # Capture stdout during test.
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        message = 'message parameter'
        input = input_helper.request_integer(message)
        self.assertEqual(input, 1)
        self.assertEqual(message + "\n", suppress_text.getvalue())
        # Re-enable stdout after test.
        sys.stdout = sys.__stdout__

    @patch('builtins.input', return_value='Y')
    def test_request_include_original_yes_pass(self, return_value):
        # Capture stdout during test.
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        input = input_helper.request_include_original()
        self.assertTrue(input)
        self.assertEqual(
            suppress_text.getvalue(),
            "Include original word? Enter 'Y'/'N' [default = 'Y']: \n")
        # Re-enable stdout after test.
        sys.stdout = sys.__stdout__

    @patch('builtins.input', return_value='N')
    def test_request_include_original_no_pass(self, return_value):
        # Capture stdout during test.
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        input = input_helper.request_include_original()
        self.assertFalse(input)
        self.assertEqual(
            suppress_text.getvalue(),
            "Include original word? Enter 'Y'/'N' [default = 'Y']: \n")
        # Re-enable stdout after test.
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main(buffer=True)
