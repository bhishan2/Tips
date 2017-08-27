"""
global imports for example_lapack.py
Copyright 2016 Ohio Supercomputer Center

Attributions:
This example was inspired by
    "Numerical Computing with Modern Fortran" (SIAM, 2013) by Hanson & Hopkins

"""
from __future__ import print_function
import argparse
import sys
import time
import logging
import numpy as np

#try:
    #import mkl
#except ImportError:
    #raise ImportError('This version of Python does not have "mkl", load with ' +
                      #'"module load python/2.7.latest"')

try:
    from scipy.linalg.lapack import dgetrf, dgetrs
    from scipy.linalg.blas import dnrm2, dgemv
except ImportError:
    raise ImportError('This version of Python does not have access to a' +
                      'lower-level lapack/blas routine.')

def main():
    """
    This example computes the following;
        1. Random number generation to fill a matrix 'a' of dimension nxn and
        also for a matrix 'y' of dimension n
        2. Pre-solve a*y = b so that we
        have 'b'.  This uses dgemv.
        3. Perform LU factorization (dgetrf) on dense matrix 'a' and store
        matrix and pivots in 'lu' and 'piv'
        4. Solve for x given 'lu' and 'piv' arrays (dgetrs)
        5. Compute L2 norm of the difference between solution and known vectors
        divided by L2 normed to the known y.  This is to provide a single point
        measure of the relative error.

    Inputs: dimension of n

    Error checks: NONE currently
    """

    # log and send it to stderr.
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("dimension", type=int, default=5, nargs='?',
                        help="The dimension of square matrix A")
    parser.add_argument("threads", type=int, default=20, nargs='?',
                        help="The number of threads")
    # grab the options here from the command line
    args = parser.parse_args()
    n = args.dimension
    #mkl.set_num_threads(args.threads)

    # begin timing random number matrix generation
    time_1 = time.time()

    logging.debug('Dimension of square n by n matrix is:' + str(n) + '\n')
    a = np.random.rand(n, n)
    y = np.random.rand(n)

    logging.debug('a:' + np.array_str(a) + '\n')
    logging.debug('y:' + np.array_str(y) + '\n')

    # begin timing LAPACK
    time_2 = time.time()

    try:
        b = dgemv(1, a, y)
    except AttributeError:
        # catch when python scipy blas does not have dgemv
        print('This version of Python does not have access to lower-level dgemv' +
              'routine.')
        sys.exit(1)

    logging.debug('b:' + np.array_str(b) + '\n')
    lu, piv, _ = dgetrf(a)  # lu factorization
    x, _ = dgetrs(lu, piv, b)  # solve for x

    logging.debug('x:' + np.array_str(x) + '\n')
    relerr = dnrm2(x-y) / dnrm2(y)

    # end timing LAPACK
    time_3 = time.time()

    #print("Solved a matrix of size:", n, "using", mkl.get_max_threads(), "threads.")
    print("Solved a matrix of size:", n, "using", 4, "threads.")
    print('Relative Error:', relerr)
    print("--- Random Matrix Generation Time: %s seconds ---" % (time_2 - time_1))
    print("---                 Solution Time: %s seconds ---" % (time_3 - time_2))

# main script begin
if __name__ == "__main__":
    main()
