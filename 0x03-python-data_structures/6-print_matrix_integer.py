#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrix_row in matrix:
        for i, num in enumerate(matrix_row):
            if i < len(matrix_row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
