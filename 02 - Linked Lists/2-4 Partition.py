from SLL import SLL
import unittest


def partition(sll, pivot):
    node = sll.head
    before_list = None
    after_list = None
    while node is not None:
        # This would be way more efficient if we kept track of list tail
        # currently it makes an O(n) call to insert every run through the
        # loop.
        if node.data < pivot:
            # Insert node into end of before list
            if before_list is None:
                before_list = SLL(node.data)
                before_end = before_list.head
            else:
                before_end = before_list.insert(node.data)
        else:
            # Insert node into end of after list
            if after_list is None:
                after_list = SLL(node.data)
            else:
                after_list.insert(node.data)

        node = node.next

    if before_list is None:
        return after_list
    
    # Merge the lists
    before_end.next = after_list.head

    return before_list

class Test(unittest.TestCase):
    cases = (
        ([9, 7, 4, 2, 4, 2, 5, 9, 4, 302, 4, 6, 1, 2, 3, 3, 8, 1111], 5),
        ([9, 7, 4, 2, 4, 2, 5, 9, 4, 302, 4, 6, 1, 2, 3, 3, 8, 1111], 1),
        ([9, 7, 4, 2, 4, 2, 5, 9, 4, 302, 4, 6, 1, 2, 3, 3, 8, 1111], 300)
    )

    def test_partition(self):
        for data, pivot in self.cases:
            test = partition(SLL(data=data), pivot)
            print(test)
            node = test.head
            output = False
            while node.data <= pivot and node.next:
                node = node.next
            while node.next:
                if node.next >= pivot:
                    output = True
                else:
                    output = False
                node = node.next
            self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()