import unittest

def palindrone_perm(string):
    """Determines whether input string is a palindrome
    
    Runs in O(n) time

    Args:
        string (string): String to be tested

    Returns:
        bool: whether string is palindrome
    """
    phrase = string.lower()
    table = [0 for ch in range(ord('z') - ord('a') + 1)]
    base = ord('a')
    oddcount = 0
    for ch in phrase:
        x = ord(ch) - base
        if x >= 0:
            table[x] += 1
            if table[x] % 2:
                oddcount += 1
            else:
                oddcount -= 1
    return oddcount <= 1


class Test(unittest.TestCase):
    data_true = (
        'tact coa',
        'level',
        'Rotator',
        'Step on no pets',
        'A man a plan a canal Panama'
    )

    data_false = (
        'not a palindrome',
        'this is wrong'
    )

    def test_palindrome(self):
        #test true
        for case in self.data_true:
            self.assertTrue(palindrone_perm(case))
        #test false
        for case in self.data_false:
            self.assertFalse(palindrone_perm(case))
        pass

if __name__ == '__main__':
    unittest.main()
    