from SLL import SLL
from random import randint
import unittest


def return_kth_to_last(sll, k):
    n1 = sll.head
    n2 = sll.head
    for _ in range(k):
        n1 = n1.next
    while n1.next:
        n1 = n1.next
        n2 = n2.next
    return n2


class Test(unittest.TestCase):

    def test_return_kth_to_last(self):
        test_array = [randint(0, 128) for i in range(100)]
        test = SLL(test_array[0])
        for i in test_array[1:]:
            test.insert(i)
        k = randint(0, 100)

        answer = test.head
        for i in range(99-k):
            answer = answer.next

        self.assertIs(return_kth_to_last(test, k), answer)


if __name__ == '__main__':
    unittest.main()
