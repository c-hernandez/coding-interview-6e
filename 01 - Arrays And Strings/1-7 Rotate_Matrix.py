import unittest

def rotate_matrix(mat):
    n = len(mat)
    return mat


class Test(unittest.TestCase):
    data = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    answer = [
        [1,8,12,16],
        [3,7,11,15],
        [2,6,10,14],
        [1,5,9,13]
    ]
    def test_rotate_matrix(self):
        output = rotate_matrix(self.data)
        self.assertEqual(output, self.answer)

if __name__ == '__main__':
    unittest.main()