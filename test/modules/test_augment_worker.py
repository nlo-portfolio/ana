#!/usr/bin/env python

import unittest
from queue import Queue
from yaml import safe_load

from modules import augment_worker


class TestAugmentWorker(unittest.TestCase):

    def setUp(self):
        self.queue_in = Queue()
        self.queue_out = Queue()
        self.config = None
        with open('config.yml', 'r') as stream:
            self.config = safe_load(stream)['settings']

    def tearDown(self):
        pass

    def test_augment_worker_pass(self):
        self.queue_in.put(('alpha'))
        self.queue_in.put(('numeric'))
        self.queue_in.put(('augmenter'))
        self.queue_in.put(None)
        augment_worker.augment(self.config, self.queue_in, self.queue_out)
        self.assertEqual(self.queue_out.get(), ('alpha\n', '4lpha\n', 'a1pha\n', 'alph4\n', '41pha\n', '4lph4\n', 'a1ph4\n', '41ph4\n'))
        self.assertEqual(self.queue_out.get(), ('numeric\n', 'num3ric\n', 'numer1c\n', 'num3r1c\n'))
        self.assertEqual(self.queue_out.get(), ('augmenter\n', '4ugmenter\n', 'au6menter\n', 'augm3nter\n', 'augment3r\n', '4u6menter\n',
                                                '4ugm3nter\n', '4ugment3r\n', 'au6m3nter\n', 'au6ment3r\n', 'augm3nt3r\n', '4u6m3nter\n',
                                                '4u6ment3r\n', '4ugm3nt3r\n', 'au6m3nt3r\n', '4u6m3nt3r\n'))
        self.assertEqual(self.queue_out.get(), None)


if __name__ == '__main__':
    unittest.main()
