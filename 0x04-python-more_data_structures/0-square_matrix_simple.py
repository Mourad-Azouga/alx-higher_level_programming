#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new=matrix.copy()
    for i in range(len(matrix)):
        new[i]=list(map(lambda x:x**2, matrix[i]))
    return(new)
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n_m=square_matrix_simple(matrix)
print(n_m)
print(matrix)