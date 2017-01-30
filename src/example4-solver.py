from sympy import *

x = Symbol('x')
result = solve(x ** 4 - 1, x)
pprint(result)
