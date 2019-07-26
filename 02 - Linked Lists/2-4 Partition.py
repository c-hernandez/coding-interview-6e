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
    #TODO: think of a good way to write a test for this since output is not necessarily sorted

    def test_partition(self):
        pass


if __name__ == '__main__':
    print('Dirty test of partitioning')
    data = [9, 7, 4, 2, 4, 2, 5, 9, 4, 302, 4, 6, 1, 2, 3, 3, 8, 1111]
    test = SLL(data[0])
    for i in data[1:]:
        test.insert(i)

    print(test)
    test = partition(test, 0)
    print(test)
