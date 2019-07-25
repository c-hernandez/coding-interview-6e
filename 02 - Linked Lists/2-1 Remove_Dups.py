from SLL import SLL
import unittest


def remove_dups(sll):
    current = sll.head
    seen = {sll.head.data}
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
    return sll


class Test(unittest.TestCase):
    def test_remove_dups(self):
        test = SLL(4)
        test_data = [4, 5, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 6, 3, 3]
        for i in test_data:
            test.insert(i)

        answer = SLL(4)
        answer_data = [5, 3, 2, 1, 6]
        for i in answer_data:
            answer.insert(i)

        print(test)
        print(remove_dups(test))
        print(answer)
        print(test == answer)
        self.assertEqual(remove_dups(test), answer)


if __name__ == '__main__':
    unittest.main()
