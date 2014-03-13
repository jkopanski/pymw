import unittest
import numpy as np
import scipy.constants as const

from pymw.lines import coaxial

class TestCorrectValues( unittest.TestCase):
    tol = 1e-3

    def test_value0( self):
        Z0 = coaxial( 3.040 * const.milli, \
                      7     * const.milli, \
                      0     * const.milli, \
                      1.0,                 \
                      1.0)
        self.assertAlmostEqual( 50.000, Z0, 1)
    def test_value1( self):
        Z0 = coaxial( 3.038 * const.milli, \
                      7     * const.milli, \
                      0.1   * const.milli, \
                      1,                   \
                      1)

        self.assertAlmostEqual( 50.000, Z0, 1)
    def test_value2( self):
        Z0 = coaxial( 3.026 * const.milli, \
                      7     * const.milli, \
                      0.2   * const.milli, \
                      1,                   \
                      1)
        self.assertAlmostEqual( 50.000, Z0, 1)
    def test_value3( self):
        Z0 = coaxial( 3.040 * const.milli, \
                      7     * const.milli, \
                      0.1   * const.milli, \
                      1,                   \
                      1)
        self.assertAlmostEqual( 49.939, Z0, 1)
    def test_value4( self):
        Z0 = coaxial( 3.040 * const.milli, \
                      7     * const.milli, \
                      0.2   * const.milli, \
                      1,                   \
                      1)
        self.assertAlmostEqual( 49.758, Z0, 1)
    def test_value5( self):
        Z0 = coaxial( 3.040 * const.milli, \
                      7     * const.milli, \
                      0.3   * const.milli, \
                      1,                   \
                      1)
        self.assertAlmostEqual( 49.453, Z0, 1)

if __name__ == '__main__':
    unittest.main()
