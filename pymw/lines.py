import numpy as np
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
