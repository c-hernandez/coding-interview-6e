from SLL import SLL
import unittest


def loop_detection(sll):
    slow = sll.head
    fast = sll.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    if not fast or not fast.next:
        return None

    slow = sll.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return fast


class Test(unittest.TestCase):

    data = (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3),
        ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], None),
        ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], None)
    )

    def build_loop(self, arr, k):
        sll = SLL(data=arr)
        tail = sll.head

        if not k:
            return sll, None

        while tail.next:
            tail = tail.next

        link = sll.head
        for _ in range(k):
            link = link.next
        tail.next = link

        return sll, link

    def test_loop_detection(self):
        for arr, k in self.data:
            case, ans = self.build_loop(arr, k)
            test = loop_detection(case)
            self.assertEqual(test, ans)


if __name__ == '__main__':
    unittest.main()
