import unittest

def zero_matrix(mat):
    """Zero rows and columns of a matrix if entry is zero

    O(nm)

    Args:
        mat: An n-by-m matrix

    Returns:
        mat: matrix with rows and columns properly zeroed
    """
    n = len(mat)
    m = len(mat[0])

    # First pass to identify zeroes
    column_zero = [0 for i in range(m)]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                mat[i][0] = 0
                column_zero[j] = 1

    # Second pass to zero out rows and columns
    for i in range(n):
        if mat[i][0] == 0:
            for j in range(m):
                mat[i][j] = 0
        else:
            for j in range(m):
                if column_zero[j]:
                    mat[i][j] = 0
    return mat

class Test(unittest.TestCase):
    data = (
        (
            [[1,2,3,4],
            [3,4,5,6],
            [0,1,2,3]],
            [[0,2,3,4],
            [0,4,5,6],
            [0,0,0,0]]
        ),
        (
            [[1,2,3,0,5,6],
            [3,4,5,2,1,0],
            [3,2,1,3,3,2],
            [2,3,6,3,1,9],
            [3,8,9,2,7,2],
            [8,7,7,1,8,2]],
            [[0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [3,2,1,0,3,0],
            [2,3,6,0,1,0],
            [3,8,9,0,7,0],
            [8,7,7,0,8,0]],
        )
    )
    def test_zero_matrix(self):
        for case,answer in self.data:
            print(case)
            self.assertEqual(zero_matrix(case),answer)

if __name__ == '__main__':
    unittest.main()