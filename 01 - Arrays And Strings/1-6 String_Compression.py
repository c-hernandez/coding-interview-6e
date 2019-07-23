import unittest

def string_compress(string):
    """Compress a string by counting repeated letters

    O(n)

    Args:
        string: string to be compressed

    Returns:
        string: compressed string if smaller, original string otherwise
    """
    count = 0
    val = string[0]
    output = []
    for char in string:
        if char != val:
            output.append(val)
            output.append(str(count))
            val = char
            count = 1
        else:
            count += 1
    output.append(val)
    output.append(str(count))

    outstring = ''.join(output)
    if len(outstring) >= len(string):
        return string
    else:
        return outstring

class Test(unittest.TestCase):
    data = (
        ('aabcccccaaa', 'a2b1c5a3'),
        ('aaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhh', 'a20h20'),
        ('abcdefg', 'abcdefg')
    )

    def test_string_compress(self):
        #test true
        for case, ans in self.data:
            self.assertEqual(string_compress(case), ans)
    
if __name__ == '__main__':
    unittest.main()
    