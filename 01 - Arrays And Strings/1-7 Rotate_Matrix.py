import unittest

def rotate_matrix(mat):
    """Rotate an n-by-n matrix clockwise 90 degrees

    O(n^2) because no matter what we have to touch every element of the matrix

    Args:
        mat: An n-by-n matrix

    Returns:
        mat: matrix rotated by 90 degrees clockwise
    """
    n = len(mat)-1
    for i in range((n+1)//2):
        for j in range(i,n-i):
            tmp = mat[i][j]
            mat[i][j] = mat[n-j][i]
            mat[n-j][i] = mat[n-i][n-j]
            mat[n-i][n-j] = mat[j][n-i]
            mat[j][n-i] = tmp
    return mat


class Test(unittest.TestCase):
    data = (
        (
            [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]],
            [[13,9,5,1], [14,10,6,2], [15,11,7,3], [16,12,8,4]]
        ),
        (
            [[1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6]],
            [[1,1,1,1,1,1],
            [2,2,2,2,2,2],
            [3,3,3,3,3,3],
            [4,4,4,4,4,4],
            [5,5,5,5,5,5],
            [6,6,6,6,6,6]]
        )
    )

    def test_rotate_matrix(self):
        for case, answer in self.data:
            self.assertEqual(rotate_matrix(case), answer)

if __name__ == '__main__':
    unittest.main()