# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTrianglesA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Scalene and Right')
    def testRightTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Scalene and Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testTrianglesA(self):
        self.assertEqual(classifyTriangle(-3, -4, 5), 'InvalidInput')
    def testTrianglesB(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput')
    def testTrianglesC(self):
        self.assertEqual(classifyTriangle(3, 4, 100), 'NotATriangle')
    def testTrianglesD(self):
        self.assertEqual(classifyTriangle(3, -4, 5), 'InvalidInput')
    def testTrianglesE(self):
        self.assertEqual(classifyTriangle(0.3, 0.4, 0.5), 'InvalidInput')
    def testTrianglesF(self):
        self.assertEqual(classifyTriangle(300, 0.4, 0.5), 'InvalidInput')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isosceles')





if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

