import unittest

from triangle import classify


class TestTriangles(unittest.TestCase):

    def testEquilateralTriangleA(self):
        self.assertEqual(classify(5, 5, 5), 'Equilateral', '5,5,5 is a Equilateral triangle')

    def testIsocelesTriangleB(self):
        self.assertEqual(classify(4, 6, 6), 'Isoceles', '4,6,6 is a Isoceles triangle')

    def testScaleneTriangleC(self):
        self.assertEqual(classify(4, 6, 9), 'Scalene', '4,6,9 is a Scalene triangle')

    def testRightTriangleF(self):
        self.assertEqual(classify(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testInvalidInputD(self):
        self.assertEqual(classify(210, 203, 209), 'InvalidInput', '210, 203, 209 return InvalidInput')

    def testInvalidInputE(self):
        self.assertEqual(classify(-6, -3, -2), 'InvalidInput', '-6, -3, -2  return InvalidInput')







if __name__ == "__main__":
    unittest.main()
