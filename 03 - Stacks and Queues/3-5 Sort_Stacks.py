from MyStack import MyStack
import unittest

def sort_stack(stack):
    data = stack.pop()
    sorted_stack = MyStack(data)
    while not stack.is_empty():
        data = stack.pop()
        count = 0
        while not sorted_stack.is_empty() and data < sorted_stack.peek() :
            stack.push(sorted_stack.pop())
            count += 1
        for _ in range(count):
            sorted_stack.push(stack.pop())
    return sorted_stack

class Test(unittest.TestCase):
    data = (
        ([2,4,6,3,7,9,8,0,1,5], [0,1,2,3,4,5,6,7,8,9]),
        ([1,2,3,1,2,3,1,2,3], [1,1,1,2,2,2,3,3,3])
    )

    def test_sort_stack(self):
        for case, actual in self.data:
            case.reverse()
            actual.reverse()
            stack = MyStack(case[0])
            for i in case[1:]:
                stack.push(i)

            ans = MyStack(actual[0])
            for i in actual[1:]:
                ans.push(i)

            test = sort_stack(stack)

            while not stack.is_empty() and not ans.is_empty():
                self.assertEqual(test.pop(), ans.pop())


if __name__ == '__main__':
    unittest.main()
