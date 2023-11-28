#!/usr/bin/python3
"""Defines a function that devides a matrix"""
def matrix_divided(matrix, div):
    """Defines a deviding function
    Args:
    matrix (list): the matrix itself
    div (int): the deviding factor
    Raises:

    TypeError: if matrix doesnt have a list inside it
    TypeError: if the rows aren't the same size
    TypeError: if div is not a number int/float
    ZeroDivisionError: if the div is 0

    Returns:
    new matrix    
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])