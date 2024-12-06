"""Clase FourVector del paquete pyforce"""

import numpy as np

class FourVector:
    def __init__(self, t, x, y, z):
        self.vector = np.array([t, x, y, z], dtype=complex)

    def __mul__(self, lorentz_transform):
        I = 1j
        AR = lorentz_transform.rep1(2)
        AL = lorentz_transform.rep2(2)
        V = np.array([[-self.vector[1] + I * self.vector[2], self.vector[3] + self.vector[0]],
                      [self.vector[3] - self.vector[0], self.vector[1] + I * self.vector[2]]], dtype=complex)
        VP = AR @ V @ AL.T
        return FourVector(
            t=np.real(VP[0, 1] - VP[1, 0]) / 2.0,
            x=np.real(VP[1, 1] - VP[0, 0]) / 2.0,
            y=np.imag(VP[0, 0] + VP[1, 1]) / 2.0,
            z=np.real(VP[0, 1] + VP[1, 0]) / 2.0
        )

    def __repr__(self):
        return f"FourVector(t={self.vector[0]}, x={self.vector[1]}, y={self.vector[2]}, z={self.vector[3]})"
