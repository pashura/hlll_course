from numpy import dot, random

from decorators import timing


@timing
def matrix_dot_matrix(x, y):
    output_matrix = []
    if not len(x[0]) <= len(y[0]):
        raise "Matrices can't be multiplied"
    for value in range(len(x)):
        line = []
        i = 0
        while i < len(y[0]):
            line.append(sum([v_x * y[i_x][i] for i_x, v_x in enumerate(x[value])]))
            i = i + 1
        output_matrix.append(line)
    return output_matrix


@timing
def matrix_dot_matrix_numpy(x, y):
    return dot(x, y)


X = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]

Y = [[1, 1, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

print(matrix_dot_matrix(X, Y))  # 1.5974044799804688e-05 sec

print(matrix_dot_matrix_numpy(X, Y))  # 1.1920928955078125e-05 sec


large_x = random.randint(0, 100, (50, 50))
large_y = random.randint(0, 100, (50, 50))


print(matrix_dot_matrix(large_x, large_y))  # 0.027988910675048828 sec

print(matrix_dot_matrix_numpy(large_x, large_y))  # 5.2928924560546875e-05 sec
