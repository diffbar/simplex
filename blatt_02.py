import numpy as np
from scipy.linalg import solve

import logging


# Simplex Tableau:
#
# +-------------------+----+
# | reduzierte Kosten | -z |
# +-------------------+----+
# | A_B^-1 * A_N      | ´b |
# +-------------------+----+

def check_feasability(T):
    m, n = np.shape(T)

    for i in range(m - 1):
        if T[i + 1] [n - 1] < 0:
            logging.error(f"LP infeasable (at {m + 1}, {n-1}")
            return False
    
    return True

def check_boundedness(T):
    m, n = np.shape(T)
    
    for i in range(n - 1):
        has_positive_val = False
        if T[0][i] <= 0:
            for j in range(m - 1):
                if T[j + 1][i] > 0:
                    has_positive_val = True
                    break
            if has_positive_val == False:
                logging.error(f"LP unbound (at column {i})")
                return False
    return True     


# Parameters:
# T (numpy.array) - Simplex tableau
def pivot_el(T):
    m, n = np.shape(T)
    
    x = {}
    # Select column for pivot operation
    for i in range(n - 1):
        x[i] = T[0][i]

    # python min returns the first item with minimal value
    s = min(x, key=x.get)

    # Select row for pivot operation
    # 1: minimum ratio rule
    x = {}
    for i in range(1, m):
        a = T[i][s]
        if a > 0:
            x[i] = T[i][n-1] / a

    r = min(x, key=x.get)

    return r, s

A = [[-3, -5, -7, 0, 0],
     [3, 5, 2, 1, 2],
     [2, 5, 3, 0, 4]]


print(A)
print(check_feasability(A))
print(check_boundedness(A))
print(pivot_el(np.array(A)))
