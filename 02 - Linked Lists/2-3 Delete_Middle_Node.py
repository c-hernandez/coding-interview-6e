from SLL import SLL
import unittest


def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next
    return node


class Test(unittest.TestCase):

    def test_delete_middle_node(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test = SLL(data=data)

        k = 5
        node = test.head
        for _ in range(k):
            node = node.next

        data.remove(k+1)
        answer = SLL(data=data)

        delete_middle_node(node)
        print(answer)
        print(test)
        self.assertEqual(test, answer)


if __name__ == '__main__':
    unittest.main()
