# -*- coding: utf-8 -*-
"""
Calcolo del determinante attraverso la regola di Laplace: costo computazionale

"""
import numpy as np

n=5
A=np.random.uniform(-1,1,(n,n))
A=np.asmatrix(A)
import timeit
tic=timeit.default_timer()
d=mydet(A)
#d=np.linalg.det(A)
toc=timeit.default_timer()
print('elapsed time is {:.4} seconds'.format(toc-tic))
