import unittest
import numpy as np
import scipy.constants as const

from pymw.lines import stripline

class TestCorrectValues( unittest.TestCase):
    tol = 1e-3

    def test_value0( self):
        Z0 = stripline( 3.049 * const.milli, \
                        0     * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        2.55)
        self.assertAlmostEqual( 30.00, Z0[0], 1)
    def test_value1( self):
        Z0 = stripline( 1.088 * const.milli, \
                        0     * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        10.20)
        self.assertAlmostEqual( 30.00, Z0[0], 1)
    def test_value2( self):
        Z0 = stripline( 1.478 * const.milli, \
                        0     * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        2.55)
        self.assertAlmostEqual( 50.00, Z0[0], 1)
    # @unittest.expectedFailure
    # def test_value3( self):
    #     Z0 = stripline( 0.375 * const.milli, \
    #                     0     * const.milli, \
    #                     2     * const.milli, \
    #                     1.0,                 \
    #                     10.20)
    #     self.assertAlmostEqual( 50.00, Z0[0], 1)
    def test_value4( self):
        Z0 = stripline( 0.708 * const.milli, \
                        0     * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        2.55)
        self.assertAlmostEqual( 75.00, Z0[0], 1)
    def test_value5( self):
        Z0 = stripline( 0.094 * const.milli, \
                        0     * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        10.20)
        self.assertAlmostEqual( 75.00, Z0[0], 1)
    def test_value6( self):
        Z0 = stripline( 2.933 * const.milli, \
                        0.03  * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        2.55)
        self.assertAlmostEqual( 30.00, Z0[0], 1)
    def test_value7( self):
        Z0 = stripline( 1.060 * const.milli, \
                        0.01  * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        10.20)
        self.assertAlmostEqual( 30.00, Z0[0], 1)
    def test_value8( self):
        Z0 = stripline( 1.397 * const.milli, \
                        0.03  * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        2.55)
        self.assertAlmostEqual( 50.00, Z0[0], 1)
    def test_value9( self):
        Z0 = stripline( 0.335 * const.milli, \
                        0.01  * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        10.20)
        self.assertAlmostEqual( 50.00, Z0[0], 1)
    def test_value10( self):
        Z0 = stripline( 0.643 * const.milli, \
                        0.03  * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        2.55)
        self.assertAlmostEqual( 75.00, Z0[0], 1)
    def test_value11( self):
        Z0 = stripline( 0.075 * const.milli, \
                        0.01  * const.milli, \
                        2     * const.milli, \
                        1.0,                 \
                        10.20)
        self.assertAlmostEqual( 75.00, Z0[0], 0)

if __name__ == '__main__':
    unittest.main()
