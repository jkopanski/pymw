import unittest
import numpy as np
import mpmath as mp
import scipy.constants as const

class TestEllipticIntegrals( unittest.TestCase):
    tol = 1e-3

    def test_value0( self):
        k  = np.sqrt( 0.00)
        m  = mp.mfrom( k = k)
        K  = mp.ellipk( m)
        Kp = mp.ellipk( 1 - m)
        self.assertAlmostEqual( 0.00, m)
        self.assertAlmostEqual( mp.mpf( 1.570796326794), K)
        self.assertEqual( mp.mpf( '+inf'), Kp)

    def test_value1( self):
        k  = np.sqrt( 0.01)
        m  = mp.mfrom( k = k)
        K  = mp.ellipk( m)
        Kp = mp.ellipk( 1 - m)
        self.assertAlmostEqual( 0.01, m)
        self.assertAlmostEqual( mp.mpf( 1.574745561317), K)
        self.assertAlmostEqual( mp.mpf( 3.695637362989), Kp)

    def test_value2( self):
        k  = np.sqrt( 0.10)
        m  = mp.mfrom( k = k)
        K  = mp.ellipk( m)
        Kp = mp.ellipk( 1 - m)
        self.assertAlmostEqual( 0.10, m)
        self.assertAlmostEqual( mp.mpf( 1.612441348720), K)
        self.assertAlmostEqual( mp.mpf( 2.578092113348), Kp)

    def test_value3( self):
        k  = np.sqrt( 0.50)
        m  = mp.mfrom( k = k)
        K  = mp.ellipk( m)
        Kp = mp.ellipk( 1 - m)
        self.assertAlmostEqual( 0.50, m)
        self.assertAlmostEqual( mp.mpf( 1.854074677301), K)
        self.assertAlmostEqual( mp.mpf( 1.854074677301), Kp)

    def test_value4( self):
        k  = np.sqrt( 0.90)
        m  = mp.mfrom( k = k)
        K  = mp.ellipk( m)
        Kp = mp.ellipk( 1 - m)
        self.assertAlmostEqual( 0.90, m)
        self.assertAlmostEqual( mp.mpf( 2.578092113348), K)
        self.assertAlmostEqual( mp.mpf( 1.612441348720), Kp)

    def test_value5( self):
        k  = np.sqrt( 0.99)
        m  = mp.mfrom( k = k)
        K  = mp.ellipk( m)
        Kp = mp.ellipk( 1 - m)
        self.assertEqual( 0.99, m)
        self.assertAlmostEqual( mp.mpf( 3.695637362989), K)
        self.assertAlmostEqual( mp.mpf( 1.574745561317), Kp)

    def test_value6( self):
        k  = np.sqrt( 1.00)
        m  = mp.mfrom( k = k)
        K  = mp.ellipk( m)
        Kp = mp.ellipk( 1 - m)
        self.assertAlmostEqual( 1.00, m)
        self.assertEqual( mp.mpf( '+inf'), K)
        self.assertAlmostEqual( mp.mpf( 1.570796326794), Kp)

if __name__ == '__main__':
    unittest.main()
