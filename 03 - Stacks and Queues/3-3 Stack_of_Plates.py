from MyStack import MyStack
import unittest


class SetOfStacks(MyStack):

    class _SubStack(MyStack):
        def __init__(self, data, max_size):
            super().__init__(self, data)
            self.max_size = max_size
            self.len = 0

        def push(self, data):
            if self.len < self.max_size:
                super().push(data)
                self.len += 1
            else:
                return False

    def __init__(self, data, max_size=10):
        super().__init__(self, data)
        self.max_size = max_size

    def push(self, data):
        if not self.head.data.push(data):
            substack = self._SubStack(data, self.max_size)
            super().push(substack)

    def pop(self):
        try:
            data = self.head.data.pop()
        except IndexError:
            super().pop()
            data = self.head.data.pop()
        return data

    def pop_at(self, idx):
        pass

    def peek(self):
        try self.peek()


class Test(unittest.TestCase):
    def test_set_of_stacks(self):
        pass


if __name__ == '__main__':
    unittest.main()
