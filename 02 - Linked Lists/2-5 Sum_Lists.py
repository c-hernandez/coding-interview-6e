from SLL import SLL
import unittest


def sum_lists(list_a, list_b):

    def sum_nodes(node_a, node_b, carry=0):
        if node_a == None and node_b == None and carry == 0:
            return None
        result = carry
        if node_a:
            result += node_a.data
        if node_b:
            result += node_b.data
        carry = result // 10
        sum_list = SLL._Node(result % 10)
        next_a = node_a.next if node_a else None
        next_b = node_b.next if node_b else None
        sum_list.next = sum_nodes(next_a, next_b, carry)
        return sum_list

    sum_list = SLL(0)
    sum_list.head = sum_nodes(list_a.head, list_b.head)

    return sum_list


class Test(unittest.TestCase):
    test = (
        ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
        ([7, 1], [5, 9, 2], [2, 1, 3]),
        ([7, 1, 9], [5, 9, 2], [2, 1, 2, 1]),
        ([7, 1, 6], [5, 9, 2, 0, 0, 1], [2, 1, 9, 0, 0, 1])
    )

    def test_sum_lists(self):
        for list_a, list_b, answer in self.test:
            a = SLL(data=list_a)
            b = SLL(data=list_b)
            ans = SLL(data=answer)
            self.assertEqual(sum_lists(a, b), ans)


if __name__ == '__main__':
    unittest.main()
