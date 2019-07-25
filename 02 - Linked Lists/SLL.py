class SLL(object):

    class _Node(object):
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self, head=None):
        self.head = self._Node(head)

    def __str__(self):
        string = ''
        current = self.head
        while current.next:
            string += str(current.data) + ','
            current = current.next
        string += str(current.data)
        return string

    def __eq__(self, other):
        current1 = self.head
        current2 = other.head

        if current1.data and current2.data:
            while current1.next and current2.next:
                if current1.data == current2.data:
                    current1 = current1.next
                    current2 = current2.next
                else:
                    return False
        else:
            return False

        if current1.next or current2.next:
            return False
        else:
            return True

    def insert(self, data):
        current = self.head
        while current.next:
            current = current.next
        current.next = self._Node(data)

    def delete(self, data):
        current = self.head

        if current.data == data:
            return self

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return self
            else:
                current = current.next
        raise Exception('Data not found in list!')
