from SLL import SLL
import unittest


def palindrome(sll):
    fast = sll.head
    slow = sll.head

    # Using a list a a stack here for simplicity.
    # I'll leave a custom implementation for the next chapter
    stack = []
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # This will skip the middle of odd sized lists
    if fast is not None:
        slow = slow.next
    
    # Now check for equality of the left and right halves
    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True



class Test(unittest.TestCase):

    def test_palindrome(self):
        cases = (
            (SLL(data=list('abcdefgfedcba')), True),
            (SLL(data=list('fasttsaf')), True),
            (SLL(data='amanaplanacanalpanama'), True),
            (SLL(data=list('notapalindrome')), False),
            (SLL(data=list('notapalindrome!')), False)
        )

        for case, answer in cases:
            print(case)
            self.assertEqual(palindrome(case), answer)



if __name__ == '__main__':
    unittest.main()
