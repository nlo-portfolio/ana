#!/usr/bin/env python

import io
import os
import unittest
import sys
from queue import Queue

from modules import file_worker


class TestFileWorker(unittest.TestCase):

    def setUp(self):
        self.append_str = 'augmented'
        self.input_filename = 'test_sample_file'
        self.output_filename = file_worker.append_str(self.input_filename, self.append_str)
        self.sample_truth = 'alpha\n4lpha\na1pha\nalph4\n41pha\n4lph4\na1ph4\n41ph4\nnumeric\nnum3ric\nnumer1c\nnum3r1c\naugmenter\n4ugmenter\nau6menter\naugm3nter\naugment3r\n4u6menter\n4ugm3nter\n4ugment3r\nau6m3nter\nau6ment3r\naugm3nt3r\n4u6m3nter\n4u6ment3r\n4ugm3nt3r\nau6m3nt3r\n4u6m3nt3r\n'
        with open(self.input_filename, 'w+') as input_file:
            input_file.write('alpha\nnumeric\naugmenter\n')

    def tearDown(self):
        pass

    def test_file_read_pass(self):
        read_queue_out = Queue()
        file_worker.read(self.input_filename, read_queue_out)
        self.assertEqual(read_queue_out.get(), ('alpha\n'))
        self.assertEqual(read_queue_out.get(), ('numeric\n'))
        self.assertEqual(read_queue_out.get(), ('augmenter\n'))


    def test_file_read_fail(self):
        # Capture stdout during test.
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        read_queue_out = Queue()
        os.remove(self.input_filename)
        with self.assertRaises(SystemExit) as cm:
            file_worker.read(self.input_filename, read_queue_out)
        self.assertEqual(cm.exception.code, 1)
        self.assertEqual("File inaccessible. Exiting.\n", suppress_text.getvalue())
        # Re-enable stdout after test.
        sys.stdout = sys.__stdout__

    # Causing broken pipe?
    def test_file_write_pass(self):
        write_queue_in = Queue()
        write_queue_out = Queue()

        write_queue_in.put(('alpha\n', '4lpha\n', 'a1pha\n', 'alph4\n', '41pha\n', '4lph4\n', 'a1ph4\n', '41ph4\n'))
        write_queue_in.put(('numeric\n', 'num3ric\n', 'numer1c\n', 'num3r1c\n'))
        write_queue_in.put(('augmenter\n', '4ugmenter\n', 'au6menter\n', 'augm3nter\n', 'augment3r\n', '4u6menter\n',
                                   '4ugm3nter\n', '4ugment3r\n', 'au6m3nter\n', 'au6ment3r\n', 'augm3nt3r\n', '4u6m3nter\n',
                                   '4u6ment3r\n', '4ugm3nt3r\n', 'au6m3nt3r\n', '4u6m3nt3r\n'))
        write_queue_in.put(None)

        file_worker.write(self.input_filename, write_queue_in, write_queue_out)

        self.assertEqual(write_queue_out.get(), ('alpha\n', '4lpha\n', 'a1pha\n', 'alph4\n', '41pha\n', '4lph4\n', 'a1ph4\n', '41ph4\n'))
        self.assertEqual(write_queue_out.get(), ('numeric\n', 'num3ric\n', 'numer1c\n', 'num3r1c\n'))
        self.assertEqual(write_queue_out.get(), ('augmenter\n', '4ugmenter\n', 'au6menter\n', 'augm3nter\n', 'augment3r\n', '4u6menter\n',
                                                 '4ugm3nter\n', '4ugment3r\n', 'au6m3nter\n', 'au6ment3r\n', 'augm3nt3r\n', '4u6m3nter\n',
                                                 '4u6ment3r\n', '4ugm3nt3r\n', 'au6m3nt3r\n', '4u6m3nt3r\n'))
        self.assertEqual(write_queue_out.get(), None)


if __name__ == '__main__':
    unittest.main()
