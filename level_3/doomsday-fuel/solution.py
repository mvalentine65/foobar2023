from __future__ import print_function
from fractions import Fraction


def gcd(a,b):
    """Given two numbers, returns the greatest common denominator"""
    while a%b != 0:
        a,b = b, a%b
    return b


def lcm(a,b):
    """Given two numbers, returns the least common multiple"""
    return a*(b/gcd(a,b))


def find_array_denominator(array):
    """Takes the int array for each state and returns the total of
    all the ints. This can be used as the denominator in the fraction
    conversion. If the denominator is zero, Sky-Net has begun
    it's assualt, and this array is a terminator array."""
    return sum(array)


def make_identity(n):
    """
    Accepts an int denoting the length of a side.
    Returns a square identity matrix with dimension n x n.
    """
    matrix = [[Fraction(0)]*n for _ in xrange(n)]
    #print_matrix(matrix, "working aug")
    for i in xrange(n):
        matrix[i][i] = Fraction(1)
    #print_matrix(matrix, "working aug")
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
    

def make_r_i_minus_q(absorbing, limited, matrix, denoms):
    """ Takes a non-standard matrix and outputs the subarrays
    R and Q according to standard form. Absorbing and limited
    are lists holding the indexes of their respective states,
    matrix is the non-standard 2-d matrix, and denoms is a
    dictionary containing indexes as keys and the number of total
    possible outcomes as the value. Returns a tuple (R,I-Q)."""
    R = list()
    Q = list()
    # make Q limited->limited array
    # why iterate over this twice when I can make I-Q here?
    for l in limited :
        #denominator d
        d = denoms[l]
        row = list()
        for ll in limited:
            row.append((l==ll)-Fraction(matrix[l][ll],d))
        Q.append(row)
    # make R limited->absorbing array
    for  l in limited:
        d = denoms[l]
        row = list()
        for a in absorbing:
            row.append(Fraction(matrix[l][a],d))
        R.append(row)
    return (R,Q)

    
def  parse_to_standardized_form(m):
    """ Given a 2-d matrix in non-standard form, returns a tuple containing
    two lists and a dictionary. The tuple[0] is a list of the indexes of all
    absorbing states, and tuple[1] is a list of the transient states. Tuple[2]
    is a dictionary containing the transient indexes and the sum of their
    elements."""
    denoms = dict()
    terminators = list()
    transients = list()
    for i in range(len(m)):
        denom = find_array_denominator(m[i])
        if denom == 0:
            terminators.append(i)
        else:
            transients.append(i)
            denoms[i] = denom
    return (terminators,transients,denoms)


def invert_matrix(matrix):
    size = len(matrix)
    matrix = augment_matrix(matrix)
    #print_augmented_matrix(matrix, "augmented:")
#    matrix.sort(reverse=True, key= lambda x: x[0])
    # row-echelon form needs non-zero values along the diagnol,
    # so ensure we have non-zero values along the diagnol
    for i in xrange(size):
        # start by swapping in the row with the highest absolute value in this position
        # this apparently helps with float precision
        # might as well do this instead of the zero check n' swap
        max_row = i
        for j in range(i + 1, size):
            if abs(matrix[i][j]) > abs(matrix[i][max_row]):
                max_row = j
        if i != max_row:
            print("swapping row " + i + " with row " + max_row)
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        #print_augmented_matrix(matrix, "working: " + str(i)) 
        # need to make zeros in column i in every row below row i
        for j in xrange(i+1, size):
            reduce_row(matrix, i, j, 0)
    
    # reduce trailing locations to 0
    for i in xrange(size - 1, -1, -1):
        for j in xrange(i):
            reduce_row(matrix, i, j, 0)
        

    # reduce rows to 1 along diagnol
    for i in xrange(size):
        reduce_row(matrix, i, i, 1)
    
    output = []
    for row in matrix:
        output.append(row[size: len(matrix[0])])

    return output


def print_matrix(matrix, name):
    print(name)
    for row in matrix:
        for i in xrange(4):
            print("{}, ".format(row[i]), end="")
        print("")
    print("")


def print_augmented_matrix(matrix, label):
    """
    Accepts a matrix and a label for printing.
    Prints the matrix with the label.
    """
    print(label + ":")
    for row in matrix:
        for i, element in enumerate(row):
            print(element, end=" ")
            if i == len(row) // 2 - 1:  # Print "|" after half of the elements
                print("|", end=" ")
        print()  # Print a newline after each row
    print()  # Print an extra newline after the matrix


def multiply_matrix(Q, R):
    output = list()
    for i in range(len(R[0])):
        total = 0
        for j in range(len(R)):
            total += Q[0][j] * R[j][i]
        output.append(total)
    return output

def make_answer(output):
    """Finds the lcm of the denominators in output. Converts the fractions to whole numbers
    and appends the lcm to the end of output."""
    least = 1
    for num in output:
        least = lcm(least,num.denominator)
    for i in range(len(output)):
        output[i] = long(output[i]*least)
    output.append(long(sum(output)))
    return output


def solution(m):
    ########################### Housekeeping ############################
    # if initial state s[0] is absorbing state, return appropriate value
    if sum(m[0]) == m[0][0]:
        return [1,1]
    terminators,transients,denoms = parse_to_standardized_form(m)
    #################### Math time ######################
    R,Q = make_r_i_minus_q(terminators,transients,m, denoms)
    Q = invert_matrix(Q)
    return make_answer(multiply_matrix(Q,R))


if __name__ == "__main__":
        case_3 = [
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ]
        answer_3 = [1, 2, 3]
        a, l, d = parse_to_standardized_form(case_3)
        R,Q = make_r_i_minus_q(a,l,case_3,d)
        #check = numpy.linalg.inv(Q)
        #print("Q:")
        #print_matrix(Q)
        #print_matrix(Q, "Q")
        inverted = invert_matrix(Q)
        print("")
        #print_matrix(check, "check")
        #print_matrix(inverted, "inverted")
        mine = make_answer(multiply_matrix(inverted, R))
        print(mine)
        sol = solution(case_3)
        assert(mine == answer_3)
        assert(sol == answer_3)
