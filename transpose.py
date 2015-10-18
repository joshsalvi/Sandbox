__author__ = 'joshsalvi'


def transpose(matrix):
    result = [[x[i] for x in matrix] for i in range(len(matrix[0]))]
    return result
