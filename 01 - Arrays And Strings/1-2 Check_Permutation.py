import unittest

def check_permutation(str1, str2):

    if len(str1) != len(str2):
        return False

    charset = [0 for i in range(128)]

    for char in str1:
        val = ord(char)
        charset[val] += 1

    for char in str2:
        val = ord(char)
        if charset[val] == 0:
            return False
        charset[val] -= 1
    return True



class Test(unittest.TestCase):
    data_true = (
        ('asdf', 'fdsa'),
        ('456789', '465879'),
        ('poci320c', 'ic320cpo')
    )

    data_false = (
        ('asdf', 'asdff'),
        ('456789', '4567890'),
        ('dwc423', 'asck3flkm')
    )

    def test_cp(self):
        for test_strings in self.data_true:
            result = check_permutation(*test_strings)
            self.assertTrue(result)

        for test_strings in self.data_false:
            result = check_permutation(*test_strings)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()