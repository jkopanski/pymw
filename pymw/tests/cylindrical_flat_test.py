import unittest
import numpy as np
import scipy.constants as const

from pymw.lines import cylindrical_flat

class TestCorrectValues( unittest.TestCase):
    tol = 1e-3
    u   = 0.548

    def test_value0( self):
        b  = 10 * const.milli
        d  = b * self.u
        Z0 = cylindrical_flat( d,   \
                               b,   \
                               1.0, \
                               1.0)
        self.assertAlmostEqual( 50.000, Z0, 0)

if __name__ == '__main__':
    unittest.main()
