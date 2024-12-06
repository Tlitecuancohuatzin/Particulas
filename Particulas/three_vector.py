#"""Clase ThreeVector del paquete pyforce"""

import numpy as np

class ThreeVector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.vector = np.array([x, y, z], dtype=complex)

    def __add__(self, other):
        return ThreeVector(*(self.vector + other.vector))

    def __sub__(self, other):
        return ThreeVector(*(self.vector - other.vector))

    def __mul__(self, scalar):
        return ThreeVector(*(self.vector * scalar))

    def dot(self, other):
        return np.dot(self.vector, other.vector)

    def cross(self, other):
        result = np.cross(self.vector, other.vector)
        return ThreeVector(*result)

    def __repr__(self):
        return f"ThreeVector(x={self.vector[0]}, y={self.vector[1]}, z={self.vector[2]})"
