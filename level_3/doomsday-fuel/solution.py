def make_identity(n):
    """
    Accepts an int denoting the length of a side.
    Returns a square identity matrix with dimension n x n.
    """
    matrix = [[0]*n]*n
    for i in range(n):
        matrix[i][i] = 1
    return matrix
            
def augment_matrix(matrix):
    """
    Adds rows of identity matrix to provided matrix.
    We don't want to track the changes to the identity separately,
    so add the rows here and extract the information later.
    """
    identity = make_identity(len(matrix))
    for y in xrange(len(matrix)):
        matrix[y] += identity[y]
    return matrix


def reduce_row(matrix, pivot, lower, value):
    """
    Subtracts pivot from lower. Makes pivot column match value.
    """
    coeff = (matrix[lower][pivot] - value) / matrix[pivot][pivot]
    for i in range(len(matrix[lower])):
        matrix[lower][i] = matrix[lower][i] - coeff*(matrix[pivot][i])
    

        
    


def _invert_matrix(matrix):
    size = length(matrix)
    matrix = augement_matrix(matrix)
#    matrix.sort(reverse=True, key= lambda x: x[0])
    # row-echelon form needs non-zero values along the diagnol,
    # so ensure we have non-zero values along the diagnol
    for i in xrange(size):
        # start by swapping in the row with the highest absolute value in this position
        # this apparently helps with float precision
        # might as well do this instead of the zero check n' swap
        max_row = i
        for j in range(i + 1, size):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        if i != max_row:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        # need to make zeros in column i in every row below row i
        for j in xrange(i+1, size):
            matrix[j] = reduce_row(matrix, i, j, 0)

    # reduce rows to 1 along diagnol
    for i in xrange(size):
        if matrix[i][i] != 1:
            for j in xrange(i):
                matrix[i][j] /= matrix[i][i]
        for y in xrange(size):
