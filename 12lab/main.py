#task1
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

#example
#matrix = Matrix(2, 3)
#print(matrix.data)
#print(matrix)

#task2

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column,value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("invalid position")

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

#example
#matrix = Matrix(2, 3)
#matrix.add_element(1, 2, 10)
#print(matrix.data)
#print(matrix)


#task3

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("Invalid position")

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            sums.append(sum(row))
        return sums

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example
#matrix = Matrix(2, 3)
#matrix.add_element(0, 0, 5)
#matrix.add_element(0, 1, 10)
#matrix.add_element(1, 2, 20)
#print(matrix.sum_of_rows())  # Output: [15, 20]


#task4

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("Invalid position")

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            sums.append(sum(row))
        return sums

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
#matrix = Matrix(2, 3)
#matrix.add_element(0, 1, 1)
#matrix.add_element(1, 2, 2)
#transposed = matrix.transpose()
#print(transposed.data)  # Output: [[0, 0], [1, 0], [0, 2]]


#task5

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("Invalid position")

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            sums.append(sum(row))
        return sums

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.columns != other.rows:
            #print("Cannot multiply matrices: incompatible dimensions")
            return None

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
#matrix1 = Matrix(2, 3)
#matrix1.add_element(0, 0, 1)
#matrix1.add_element(0, 1, 2)
#matrix1.add_element(0, 2, 3)

#matrix2 = Matrix(3, 2)
#matrix2.add_element(0, 0, 1)
#matrix2.add_element(1, 0, 2)
#matrix2.add_element(2, 0, 3)

#result = matrix1.multiply_by(matrix2)
#print(result.data)  # Output: [[14, 0], [0, 0]]

#task6

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("Invalid position")

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            sums.append(sum(row))
        return sums

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.columns != other.rows:
            #print("Cannot multiply matrices: incompatible dimensions")
            return None

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def is_symmetric(self):
        return self == self.transpose()

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
#matrix = Matrix(2, 2)
#matrix.add_element(0, 1, 5)
#matrix.add_element(1, 0, 5)
#print(matrix.is_symmetric())  # Output: True



#task7


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("Invalid position")

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            sums.append(sum(row))
        return sums

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.columns != other.rows:
            #print("Cannot multiply matrices: incompatible dimensions")
            return None

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def is_symmetric(self):
        return self == self.transpose()

    def rotate_right(self):
        self.data = self.transpose().data
        for i in range(self.rows):
            self.data[i] = self.data[i][::-1]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
#matrix = Matrix(2, 2)
#matrix.add_element(0, 0, 1)
#matrix.add_element(0, 1, 2)
#matrix.add_element(1, 0, 3)
#matrix.add_element(1, 1, 4)
#matrix.rotate_right()
#print(matrix.data)  # Output: [[3, 1], [4, 2]]


#task8

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("Invalid position")

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            sums.append(sum(row))
        return sums

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.columns != other.rows:
            #print("Cannot multiply matrices: incompatible dimensions")
            return None

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def is_symmetric(self):
        return self == self.transpose()

    def rotate_right(self):
        self.data = self.transpose().data
        for i in range(self.rows):
            self.data[i] = self.data[i][::-1]

    def flatten(self):
        return [element for row in self.data for element in row]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
#matrix = Matrix(2, 2)
#matrix.add_element(0, 0, 1)
#matrix.add_element(0, 1, 2)
#matrix.add_element(1, 0, 3)
#matrix.add_element(1, 1, 4)
#print(matrix.flatten())  # Output: [1, 2, 3, 4]


#task9

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("Invalid position")

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            sums.append(sum(row))
        return sums

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.columns != other.rows:
            #print("Cannot multiply matrices: incompatible dimensions")
            return None

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def is_symmetric(self):
        return self == self.transpose()

    def rotate_right(self):
        self.data = self.transpose().data
        for i in range(self.rows):
            self.data[i] = self.data[i][::-1]

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        if rows == 0:
            return Matrix(0, 0)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        for i in range(rows):
            for j in range(columns):
                matrix.data[i][j] = list_of_lists[i][j]
        return matrix

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
#list_of_lists = [[1, 2], [3, 4]]
#matrix = Matrix.from_list(list_of_lists)
#print(matrix.data)  # Output: [[1, 2], [3, 4]]


#task10

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        #else:
            #print("Invalid position")

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            sums.append(sum(row))
        return sums

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.columns != other.rows:
            #print("Cannot multiply matrices: incompatible dimensions")
            return None

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def is_symmetric(self):
        return self == self.transpose()

    def rotate_right(self):
        self.data = self.transpose().data
        for i in range(self.rows):
            self.data[i] = self.data[i][::-1]

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        if rows == 0:
            return Matrix(0, 0)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        for i in range(rows):
            for j in range(columns):
                matrix.data[i][j] = list_of_lists[i][j]
        return matrix

    def diagonal(self):
        if self.rows != self.columns:
            #print("Matrix is not square")
            return None

        return [self.data[i][i] for i in range(self.rows)]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
#matrix = Matrix(3, 3)
#matrix.add_element(0, 0, 1)
#matrix.add_element(1, 1, 2)
#matrix.add_element(2, 2, 3)
#print(matrix.diagonal())  # Output: [1, 2, 3]
