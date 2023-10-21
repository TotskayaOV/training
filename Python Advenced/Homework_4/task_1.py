# Напишите функцию для транспонирования матрицы


def transposition_matrix(matrix_input: list) -> list:
    matrix_output = [[0 for _ in range(len(matrix_input))] for _ in range(len(matrix_input[0]))]
    for i in range(len(matrix_input)):
        for j in range(len(matrix_input[0])):
            matrix_output[j][i] = matrix_input[i][j]
    return matrix_output


if __name__ == '__main__':
    user_matrix = [[1, 2, 3], [3, 4, 5], [6, 7, 8], [9, 0, 1]]
    for vector in (transposition_matrix(user_matrix)):
        print(vector)
