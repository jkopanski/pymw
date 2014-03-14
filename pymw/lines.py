import numpy as np
import mpmath as mp
import scipy.constants as const

def coaxial( a, b, c=0.0, mu=1.0, eps=1.0):
    """Calculate impedance of coaxial line

    Paramters
    ---------
    a : float
        Diameter of inner wire
    b : float
        Diameter of outer wire
    c : float
        Innrer wire skew from center position
    mu : float
        Relative permeability of the dielectric material filling the line
    eps : float
        Relative permittivity of the dielectric material filling the line

    Returns
    -------
    Z0 : float
        Characteristic impedance of the line
    """
    if c == 0.0:
        Z0 = 59.952 * np.sqrt( mu / ( eps)) * np.log( b / a)
        #np.sqrt( const.mu_0 * mu / ( const.epsilon_0 * eps)) * np.log( b / a) / ( 2 * const.pi)
    else:
        x =  ( a + ( b ** 2 - 4 * c ** 2) / a) / ( 2 * b)
        Z0 = 59.952 * np.sqrt( mu / eps) * np.log( x + np.sqrt( x ** 2 - 1))
    return Z0

def cylindrical_flat( d, b, mu=1.0, eps=1.0):
    """Calculate impedance of cylindrical flat line

    Paramters
    ---------
    d : float
        Diameter of inner wire
    b : float
        Distance between outer parallel plates
    mu : float
        Relative permeability of the dielectric material filling the line
    eps : float
        Relative permittivity of the dielectric material filling the line

    Returns
    -------
    Z0 : float
        Characteristic impedance of the line
    """
    u = d / b
    r = const.pi * u / 4
    x = 1 + 2 * np.sinh( r) ** 2
    y = 1 - 2 * np.sin( r) ** 2
    Z0 = 59.952 * \
         np.sqrt( mu / eps) * \
         ( np.log( ( np.sqrt( x) + np.sqrt( y)) / np.sqrt( x - y)) \
           - r ** 4 / 30 \
           + 0.014 * r ** 8)
    return Z0

def stripline( w, t, b, mu=1.0, eps=1.0):
    """Calculate impedance of stripline

    Paramters
    ---------
    w : float
        Width of inner wire
    t : float
        Thickness of inner wire
    b : float
        Distance between outer parallel plates
    mu : float
        Relative permeability of the dielectric material filling the line
    eps : float
        Relative permittivity of the dielectric material filling the line

    Returns
    -------
    Z0 : float
        Characteristic impedance of the line
    """
    if t != 0:
        m  = 6 * ( b - t) / ( 3 * b - t)
        dW = t * ( 1 - 0.5 * \
                   np.log( ( t / ( 2 * b - t)) ** 2 + \
                           ( 0.0796 * t / ( w + 1.1 * t)) ** m)) / const.pi
        a  = 4 * ( b - t) / ( const.pi * ( w + dW))
        Z0 = 30.0 * np.log( 1 + a * \
                            ( 2 * a + np.sqrt( 4 * a ** 2 + 6.27))) / np.sqrt( eps)
    else:
        k  = 1 / np.cosh( const.pi * w / ( 2 * b))
        Z0 = 29.976 * const.pi * np.sqrt( mu / eps) / ( mp.mpc( -1j) * mp.taufrom( k = k))
        #* mp.ellipk( k) / mp.ellipk( np.sqrt( 1 - k ** 2)) 
    return Z0
