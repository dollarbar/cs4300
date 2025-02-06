# This program uses the numpy package to generate a matrix
# with random values in a certain number of rows and columns
# Just in case someone needs a matrix with the same amoutn of rows
# as there are columns, this program tests for that very case.

import numpy as np


# type in how many rows and columns you want in your matrix
num_rows = 5
num_cols = 5

# matrix should be num_rows x num_cols matrix
matrix = np.random.rand(num_rows,num_cols)


def test_matrix_row_column_equality():

    # .shape attribute to matrix returns number of rows and cols in matrix
    num_rows, num_cols = matrix.shape

    # test for equality between rows and cols.
    assert num_rows == num_cols

