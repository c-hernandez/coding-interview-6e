import unittest

def urlify(str, truelen):
    arr = list(str)
    startpos = len(arr)-1
    for char in range(0,truelen-1):
        if arr[char] == ' ':
            startpos -= 2

    pos = len(arr)-1

    for ind in range(startpos, -1, -1):
        char = arr[ind]
        if char == ' ':
            arr[pos-2:pos+1] = ['%', '2', '0']
            pos -= 3
        else:
            arr[pos] = char
            pos -= 1

    return ''.join(arr)

        

class Test(unittest.TestCase):
    test_cases = [
        ('Mr John Smith    ', 13, "Mr%20John%20Smith"),
        ('Mrs Jane Doe    3            ', 17, "Mrs%20Jane%20Doe%20%20%20%203")
    ]

    def test_urlify(self):
        for case, length, answer in self.test_cases:
            self.assertEqual(urlify(case, length), answer)

if __name__ == "__main__":
    unittest.main()