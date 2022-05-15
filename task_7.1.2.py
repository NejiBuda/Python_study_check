class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(lambda r: "  ".join(map(str, r)), self.matrix)) + "\n"

    def __add__(self, other):
        return Matrix(map(lambda res_1, res_2: map(lambda x, y: x + y, res_1, res_2), self.matrix, other.matrix))

metd_1 = Matrix([[3, 5, 8], [3, 8, 3], [7, 1, 5]])
metd_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(metd_1)
print(metd_2)
r = metd_1 + metd_2
print(r)
