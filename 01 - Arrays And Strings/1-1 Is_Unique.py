import unittest

def unique(str):
    if len(str) > 128:
        return False
    
    charset = [False for i in range(128)]
    for char in str:
        val = ord(char)
        if charset[val]:
            return False
        charset[val] = True

    return True

class Test(unittest.TestCase):
    data_true = [('abcd'), ('sf4ecla38'), ('')]
    data_false = [('sakvidowd'), ('parallel')]

    def test_unique(self):
        for test_string in self.data_true:
            actual = unique(test_string)
            self.assertTrue(actual)
        for test_string in self.data_false:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()