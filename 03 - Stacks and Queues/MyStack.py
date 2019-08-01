class MyStack:

    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, data):
        self.head = self._Node(data)

    def pop(self):
        if self.head == None:
            raise IndexError('Stack is empty!')
        node = self.head
        self.head = self.head.next
        return node.data

    def push(self, data):
        node = self._Node(data)
        node.next = self.head
        self.head = node

    def peek(self):
        if self.head == None:
            raise IndexError('Stack is empty!')
        return self.head.data

    def is_empty(self):
        return self.head == None
