#!/usr/bin/python3
"""let's maje a triangle"""


def pascal_triangle(n):
    """this function should do the trick"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tempo = [1]
        for i in range(len(tri) - 1):
            tempo.append(tri[i] + tri[i + 1])
        tempo.append(1)
        triangles.append(tempo)
    return triangles