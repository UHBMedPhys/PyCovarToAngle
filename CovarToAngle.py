#  """
#  Copyright 2024 Antony Carver, University Hospitals Birmingham NHS Foundation Trust
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  """

import math

import numpy as np


class CorrelationMatrix:
    def __init__(self, d=1):
        # create an n-dimensional correlation matrix
        self.correlation_matrix = np.identity(d)
        self.dims = d

    def set_shape(self, d):
        self.dims = d
        self.correlation_matrix = np.identity(d)

    def set_element(self, i, j, val):
        if i < self.dims and j < self.dims:
            v_old = self.correlation_matrix[i, j]
            self.correlation_matrix[i, j] = val
            #now validate and relpace if not

    def set_matrix(self, mat):
        if len(mat.shape) != 2:
            return

        if mat.shape[0] == self.dims and mat.shape[1] == self.dims:
            self.correlation_matrix = mat
            # again need to create a validator

    def matrix_to_chol(self):
        # make this very verbose at first
        if self.dims == 1:
            return 1
        else:
            return np.linalg.cholesky(self.correlation_matrix)

    def chol_to_matrix(self, B):
        return B @ B.transpose()

    def angles_to_matrix(self, ang):
        # completely verbose to start with, can tidy it up later
        #  print(ang)
        B = np.zeros((self.dims, self.dims))
        B[0, 0] = 1

        Angles = np.zeros((self.dims, self.dims))
        counter = 0
        for i in range(1, self.dims):
            for j in range(0, i):
                Angles[i, j] = ang[counter]
                counter = counter + 1

        if int(self.dims * (self.dims - 1) / 2) != ang.shape[0]:
            print("Array not the right size!")

        for i in range(1, self.dims):
            cum_sine = 1
            for j in range(0, i + 1):
                if i == j:
                    B[i, j] = cum_sine
                else:
                    B[i, j] = cum_sine * np.cos(Angles[i, j])
                    cum_sine = cum_sine * np.sin(Angles[i, j])

        # print(self.chol_to_matrix(B))
        return self.chol_to_matrix(B)

    def get_thetas(self):
        # again make this painfully explicit to start with
        # get B to start with
        B = self.matrix_to_chol()
        out = list()
        print('B:', B)
        if self.dims == 2:
            print("Returning")
            return np.array([np.arccos(B[1, 0])])
        for i in range(1, self.dims):
            print("here")
            cum_sinarccos = 1
            for j in range(0, i):
                if j == 0:
                    print(i, j, (B[i, j]))
                    out.append(np.arccos(B[i, j]))
                    cum_sinarccos = cum_sinarccos * np.sin(np.arccos(B[i, j]))
                else:
                    print(i, j, (B[i, j]))
                    out.append(np.arccos(B[i, j] / cum_sinarccos))
                    cum_sinarccos = cum_sinarccos * np.sin(np.arccos(B[i, j]))

        return np.array(out)

    def test_parameterisation(self):
        angles = np.array([1.5, 0.4, 2.5])
        print(angles.shape)
        return self.angles_to_matrix(angles)

    def test_parameterisation_b(self):
        angles = np.array([1.5, 0.4, -1.5])
        print(angles.shape)
        return self.angles_to_matrix(angles)


corr_test = CorrelationMatrix(3)
matrix = corr_test.test_parameterisation()

corr_test_2 = CorrelationMatrix(3)
corr_test_2.set_matrix(matrix)
print(corr_test_2.get_thetas())

corr_test_b = CorrelationMatrix(3)
matrix = corr_test_b.test_parameterisation_b()

corr_test_2_b = CorrelationMatrix(3)
corr_test_2_b.set_matrix(matrix)
print(corr_test_2_b.get_thetas())
