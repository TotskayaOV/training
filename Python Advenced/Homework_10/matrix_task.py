class Matrix:

    def __init__(self, mtx_list: list):
        self.mtx = self._check_matrix(mtx_list)
        self.rows = len(mtx_list)
        self.columns = len(mtx_list[0])
        print(self.columns)

    def _check_matrix(self, mtx_list):
        for i in range(0, len(mtx_list) - 1):
            if len(mtx_list[i]) == len(mtx_list[i+1]):
                continue
            else:
                raise ValueError
        return mtx_list

    def get_matrix(self):
        return self.mtx

    def transposition_matrix(self):
        matrix_output = [[0 for _ in range(len(self.mtx))] for _ in range(len(self.mtx[0]))]
        for i in range(len(self.mtx)):
            for j in range(len(self.mtx[0])):
                matrix_output[j][i] = self.mtx[i][j]
        return matrix_output

    def __str__(self):
        return '\n'.join(str(x) for x in self.mtx)

    def __repr__(self):
        return f"Matrix({', '.join(str(x) for x in self.mtx)})"

    def transposition_matrix_to_str(self):
        return '\n'.join(str(x) for x in self.transposition_matrix())

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                matrix_output = [[0 for _ in range(len(self.mtx[0]))] for _ in range(len(self.mtx))]
                for i in range(len(self.mtx)):
                    for j in range(len(self.mtx[i])):
                        matrix_output[i][j] = self.mtx[i][j] + other.mtx[i][j]
                return Matrix(matrix_output)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns == other.rows:
                return list(map(lambda x: list(map(lambda y: sum(i * j for i, j in zip(x, y)),
                                                   zip(*other.mtx))), self.mtx))
        if isinstance(other, int | float):
            return [[element * other for element in row] for row in self.mtx]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                for i in range(self.rows):
                    for j in range(self.columns):
                        if self.mtx[i][j] != other.mtx[i][j]:
                            return False
                        return True
        return False


if __name__ == '__main__':
    obj_1 = Matrix([[1, 12, 3], [14, 5, 6]])
    print(obj_1)
    print(obj_1.transposition_matrix_to_str())
    obj_2 = Matrix([[1, 12, 3], [14, 5, 6]])
    print(obj_1 * obj_2)
    print(obj_1 * 2)
    print(obj_1 + obj_2)
    print(obj_1 == obj_2)
