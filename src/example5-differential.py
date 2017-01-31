import numpy as np
from sympy import *


def robot_model(vr, vl):
    R = 1
    L = 2
    V = R * (vr + vl) / 2
    W = R * (vr - vl) / L
    return np.array([V, W])


def robot_matrix_model():
    R = Symbol('R')
    L = Symbol('L')
    A = R * Matrix([[1 / 2., 1 / 2.], [1 / L, -1 / L]])
    return A


A_robot = robot_matrix_model()
pprint(A_robot)
A_robot_inv = A_robot.inv()
pprint(A_robot_inv)
