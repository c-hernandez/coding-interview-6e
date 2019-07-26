from SLL import SLL
import unittest


def sum_lists(list_a, list_b):
    a = list_a.head
    b = list_b.head
    output = SLL(a.data+b.data % 10)
    carry = a.data+b.data // 10
    while a.next or b.next:
        c = a.next.data + b.next.data + carry
        output.insert(c % 10)
        carry = c // 10
        a = a.next
        b = b.next
    return output


class Test(unittest.TestCase):
    test = (
        (([7,1,6],[5,9,2]),[2,1,9]),
        (([7,1,6],[5,9,2]),[2,1,9]),
        (([7,1,6],[5,9,2]),[2,1,9]),
        (([7,1,6],[5,9,2]),[2,1,9])
    )
    def test_sum_lists(self):
        pass

if __name__ == '__main__':
    unittest.main()
