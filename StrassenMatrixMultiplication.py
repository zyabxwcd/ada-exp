a = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
b = [[4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1]]


def generate_matrix(p, q):  # create a matrix filled with 0s
    matrix = [[0 for row in range(p)] for col in range(q)]
    return matrix


def split(matrix):  # split matrix into quarters
    a = matrix
    b = matrix
    c = matrix
    d = matrix

    # Top half rows go into a and b, while bottom half into c and d
    while(len(a) > len(matrix)/2):
        a = a[:len(a)//2]
        b = b[:len(b)//2]
        c = c[len(c)//2:]
        d = d[len(d)//2:]

    # First half of top half rows go into a
    # Second half of top half into b
    # Similarly for c and d
    while(len(a[0]) > len(matrix[0])/2):
        for i in range(len(a[0])//2):
            a[i] = a[i][:len(a[i])//2]
            b[i] = b[i][len(b[i])//2:]
            c[i] = c[i][:len(c[i])//2]
            d[i] = d[i][len(d[i])//2:]
    return a, b, c, d

# Normal matrix addition


def add_m(a, b):
    if type(a) == int:
        d = a + b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] + b[i][j])
            d.append(c)
    return d

# Normal matrix subtraction


def sub_m(a, b):
    if type(a) == int:
        d = a - b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] - b[i][j])
            d.append(c)
    return d


def strassen_multiply(a, b, q):
    # base case: 1x1 matrix
    if q == 1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]
        return d
    else:
        # split matrices into quarters
        a11, a12, a21, a22 = split(a)
        b11, b12, b21, b22 = split(b)

        # p1 = (a11+a22) * (b11+b22)
        p1 = strassen_multiply(add_m(a11, a22), add_m(b11, b22), q/2)

        # p2 = (a21+a22) * b11
        p2 = strassen_multiply(add_m(a21, a22), b11, q/2)

        # p3 = a11 * (b12-b22)
        p3 = strassen_multiply(a11, sub_m(b12, b22), q/2)

        # p4 = a22 * (b12-b11)
        p4 = strassen_multiply(a22, sub_m(b21, b11), q/2)

        # p5 = (a11+a12) * b22
        p5 = strassen_multiply(add_m(a11, a12), b22, q/2)

        # p6 = (a21-a11) * (b11+b12)
        p6 = strassen_multiply(sub_m(a21, a11), add_m(b11, b12), q/2)

        # p7 = (a12-a22) * (b21+b22)
        p7 = strassen_multiply(sub_m(a12, a22), add_m(b21, b22), q/2)

        '''
       Resultant product matrix ‘c’ is composed of 4 sub matrices c11, c12, c21, 
       c22.
       '''

        # c11 = p1 + p4 - p5 + p7
        c11 = add_m(sub_m( add_m(p1, p4), p5), p7)

        # c12 = p3 + p5
        c12 = add_m(p3, p5)

        # c21 = p2 + p4
        c21 = add_m(p2, p4)

        # c22 = p1 + p3 - p2 + p6
        c22 = add_m(sub_m( add_m(p1, p3), p2), p6)
        c = generate_matrix(len(c11)*2, len(c11)*2)

        # Combine resultant sub-matrices c11, c12, c21, c22 into a single product
        # matrix ‘c’
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j] = c11[i][j]
                # For merging c12, c21, c22 into c at correct positions, size of a
                # single sub matrix or size of c11 is added to the position index.
                c[i][j+len(c11)] = c12[i][j]
                c[i+len(c11)][j] = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c


print('Input Matrices:')
print('A:', a)
print('B:', b)
print("Matrix Product:")
print(strassen_multiply(a, b, 4))
