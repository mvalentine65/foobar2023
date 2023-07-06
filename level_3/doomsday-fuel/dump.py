import fractions
def transpose(matrix):
    return map(list,zip(*matrix))


def make_minor_matrix(matrix,y,x):
    return [row[:x] + row[x+1:] for row in (matrix[:y]+matrix[y+1:])]

case_2 = [  [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0] ]

def make_determinant(matrix):
    #base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1)**c)*matrix[0][c]*make_determinant(make_minor_matrix(matrix,0,c))
    return determinant

def matrix_inverse_expansion(matrix):
    determinant = make_determinant(matrix)
    #special case for 2x2 matrix:
    if len(matrix) == 2:
        return [[matrix[1][1]/determinant, -1*matrix[0][1]/determinant],
                [-1*matrix[1][0]/determinant, matrix[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for row in range(len(matrix)):
        cofactorRow = []
        for column in range(len(matrix)):
            minor = make_minor_matrix(matrix,row,column)
            cofactorRow.append(((-1)**(row+column)) * make_determinant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for row in range(len(cofactors)):
        for column in range(len(cofactors)):
            cofactors[row][column] = cofactors[row][column]/determinant
    return cofactors


Q_2 = [[1,0-fractions.Fraction(2,3)],[0,1]]
Q_1 = [[1,fractions.Fraction(-1,2)],
                [fractions.Fraction(-4,9),1]]
print(matrix_inverse_expansion(Q_2))
print(matrix_inverse_expansion(Q_1))