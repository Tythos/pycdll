"""Tests the platform-specific C library built from test.c
"""

import unittest
import platform
import os
from ctypes import cdll

class DllTest(unittest.TestCase):
    def test_sum(self):
        if platform.system() == 'Windows':
            dllPath = 'test.dll'
        else:
            dllPath = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'test.so'
        if not os.path.exists(dllPath):
            raise Exception('Build library "%s" before running test' % dllPath)
        mydll = cdll.LoadLibrary(dllPath)
        self.assertEquals(mydll.sum(1,2),3)
        
if __name__ == '__main__':
    unittest.main()
