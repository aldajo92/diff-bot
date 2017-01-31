from sympy import *

x = Symbol('x')
y = Symbol('y')
A = Matrix([[1, x], [y, 1]])

pprint(A)
pprint(Integral(x ** 2 / 2, x))

B = 2*A
pprint(B)