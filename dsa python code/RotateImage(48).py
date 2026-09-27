def rotate(matrix):
    matrix[:] = [list(row)[::-1] for row in zip(*matrix)]