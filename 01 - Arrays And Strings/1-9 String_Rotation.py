import unittest

def is_substring(string1, string2):
    return string1 in string2

def string_rotation(string1, string2):
    """Determine if one string is a rotation of another

    Speed depends on the implementation of the search in is_substring

    Args:
        string1: string to find
        string2: possibly rotated string

    Returns:
        bool: whether string2 is a rotation of string1
    """
    return is_substring(string1, string2*2)

    

class Test(unittest.TestCase):
    data = (
        (('waterbottle', 'erbottlewat'), True),
        (('waterbottle', 'notterbottle'), False)
    )
    def test_string_rotation(self):
        for case, answer in self.data:
            self.assertEqual(string_rotation(*case), answer)

if __name__ == '__main__':
    unittest.main()