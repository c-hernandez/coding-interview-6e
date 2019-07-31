from SLL import SLL
import unittest


def intersection(list_a, list_b):
    # Determine if there's an intersection and record the lengths
    len_a = 0
    node_a = list_a.head
    while node_a.next:
        len_a += 1
        node_a = node_a.next

    len_b = 0
    node_b = list_b.head
    while node_b.next:
        len_b += 1
        node_b = node_b.next

    # return false if there is no intersection
    if node_a is not node_b:
        return False

    # take the difference of the lengths
    diff = len_a - len_b
    node_a = list_a.head
    node_b = list_b.head

    # move the longer list forward to match the distance to intersection
    if diff > 0:
        for _ in range(abs(diff)):
            node_a = node_a.next
    elif diff < 0:
        for _ in range(abs(diff)):
            node_b = node_b.next

    # find the intersection
    while node_a.next is not node_b.next:
        node_a = node_a.next
        node_b = node_b.next

    # return the intersecting node
    return node_a.next


class Test(unittest.TestCase):

    data = (
        ([1,2,3,4,5,6,7,8,9], [10,11,12], 2),
        ([1,2,3,4,5,6,7,8,9], [10,11,12], 6),
        ([1,2,3,4,5,6,7,8,9], [10,11,12], 8),
        ([1,1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,2,], None)
    )

    def build_intersecting_lists(self, arr1, arr2, idx=None):
        list_1 = SLL(data=arr1)
        list_2 = SLL(data=arr2)

        if idx is None:
            return list_1, list_2, False

        link_node  = list_1.head
        tail_node  = list_2.head

        for _ in range(idx):
            link_node = link_node.next

        while tail_node.next:
            tail_node = tail_node.next

        tail_node.next = link_node

        return list_1, list_2, link_node


    def test_intersection(self):
        for arr_1, arr_2, link in self.data:
            L1, L2, ans = self.build_intersecting_lists(arr_1, arr_2, idx=link)
            print(str(L1), str(L2))
            output = intersection(L1, L2)
            self.assertEqual(output, ans)

if __name__ == '__main__':
    unittest.main()
