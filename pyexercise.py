import sympy as sy
import numpy as np

def fun_1( my_id ):
    ans = hex(my_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(-x/2), (x,4, sy.oo))
    return ans

def my_solution():
    A = np.array( [[7,64,36,44,72,82,96,46,100,35], [44,47,34,84,94,36,84,68,7,10],
                   [98,46,53,48,66,8,60,53,82,98], [26,80,12,21,88,48,47,46,82,84],
                   [20,50,24,54,39,75,2,34,54,70], [6,40,12,92,13,25,48,28,22,66],
                   [20,76,74,39,42,96,71,22,60,44], [36,66,13,44,18,70,88,29,8,22],
                   [56,77,96,92,80,66,60,42,83,12], [29,14,40,78,30,64,56,78,22,21]] )
    b = np.array([96,76,26,58,92,46,12,88,92,58])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    my_id = 1203222
    print('Hexadecimal representation of %d is %s'%( my_id, fun_1( my_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
