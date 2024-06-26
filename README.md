# PyCovarToAngle
This repository is primarily a test-bed for our public github repos (although the code here should work as intended).
Python implementation of a Covariance matrix parameterisation

This is a Python implementation of:
Distribution of random correlation matrices: Hyperspherical parameterization of the Cholesky factor
Mohsen Pourahmadi and Xiao Wang
Statistics & Probability Letters, 2015, vol. 106, issue C, 5-12

# Purpose
This implements a the hyperspherical paramterisation of the covariance matrix.
For large non-linear optimisation problems estimation of the covariance matrix is challenging.
This reduces the optimiation problem of an nxn covariance matrix to (n^2/2)-1 independent values that can be found via bounded optimisation between 0 and pi.

# Setup
This package requires numpy

