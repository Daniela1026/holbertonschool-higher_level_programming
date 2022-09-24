#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for m_one in range(len(matrix)):
            for m_two in range(len(matrix[m_one])):
                if m_two is not len(matrix[m_one])-1:
                    print("{:d} ".format(matrix[m_one][m_two]), end='')
                else:
                    print("{:d}".format(matrix[m_one][m_two]), end='')
            print()
