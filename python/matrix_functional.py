def my_matrix_sum(m1, m2):
    '''m1 : m*n matrix, m2 : m*n matrix) \n
        returns a m*n matrix which is the matrix sum of m1 and m2'''

    m = len(m1)
    n = len(m1[0])
    return [[m1[i][j] + m2[i][j] for j in range(n)] for i in range(m)]


def column_to_row(cv):
    '''
    cv : n*1 column vector \n
    returns a 1*n row vector
    '''
    rv = []

    for row in cv:
        rv.append(row[0])

    return rv


def my_vm_product(A, v):
    '''
    A: m*n matrix, v: n*1 vector
    retruns the matrix-vector product of A and v
    '''

    m = len(A)
    n = len(v)

    ans = []

    for i in range(m):

        sum = 0
        for j in range(n):
            sum += A[i][j]*v[j][0]

        ans.append([sum])

    return ans


def my_transpose(M):
    '''
    M : m*n matrix
    returns the transpose of M, which is a n*m matrix
    '''
    m = len(M)
    n = len(M[0])

    N = [[(0) for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            N[i][j] = M[j][i]

    return N


def sorted(lon):
    '''
    lon: list of numbers
    returns True if the lon is sorted in ascending order
    otherwise returns False
    '''

    n = len(lon)

    for i in range(n-1):
        if lon[i] > lon[i+1]:
            return False

    return True


# Driver code to test the functions
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 8, 9]
]

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [0, 0, 0],
    [1, 1, 1],
    [3, 2, 1]
]

n = [[1], [2], [3]]


print(my_matrix_sum(m1, m2))
print(column_to_row(n))
print(my_vm_product(m1, n))
print(my_vm_product(m2, n))
print(my_transpose(m))
print(my_transpose(m1))
print(my_transpose(m2))

print(sorted([1, 2, 5, 6]))
print(sorted([1, 2, 5, 4]))
print(sorted([9, 2, 5, 6]))
print(sorted([2, 5, 5, 6]))
print(sorted([9, 10, 11, 12, 2, 12, 13, 14]))
