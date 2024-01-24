#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        i = len(matrix)
        b = []
        for z in range(i):
            q = []
            for r in matrix[z]:
                sqr = r * r
                q.append(sqr)
            b.append(q)
    return (b)
