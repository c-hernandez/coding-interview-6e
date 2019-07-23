import unittest

def one_away(str1, str2):
    """Determines whether a string is one edit away from another

    O(n)

    Args:
        str1 (string): First string to be compared
        str2 (string): Second string to be compared
    
    Returns:
        bool: Whether str2 is one edit away from str1
    """
    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        return check_change(str2, str1)
    elif len2 > len1:
        return check_change(str1, str2)
    else:
        mod = 0
        for i in range(len1):
            if str1[i] != str2[i]:
                mod += 1
                if mod < 1:
                    return False

    return True

def check_change(str1, str2):
    change = 0
    for i in range(len(str1)):
        if str1[i] != str2[i+change]:
            change += 1
            if change > 1:
                return False
    return True

class Test(unittest.TestCase):
    data_true = (
        ('pale', 'ple'),
        ('pales', 'pale'),
        ('pale', 'bale'),
        ('lake', 'slake')
    )
    data_false = (
        ('pale', 'bake'),
        ('sale', 'shales')
    )

    def test_one_away(self):
        #test true
        for str1,str2 in self.data_true:
            self.assertTrue(one_away(str1, str2))
        #test false
        for str1,str2 in self.data_false:
            self.assertTrue(one_away(str1, str2))
        
if __name__ == '__main__':
    unittest.main()
    