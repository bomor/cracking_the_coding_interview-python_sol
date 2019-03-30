import pytest
from chapter2.node import Node
from stack_and_queue import Stack


# In this Approach, each node in the stack keeps a track of
# the minimum beneath itself.
# NOTE: If we have a large stack, we waste a lot of space
# by keeping a track of the min for every single element.

class StackWithMin(Stack):

    def push(self, val):
        if self.top:
            minimum = min(val, self.top.min)
            new_top = StackNode(val, minimum)
            new_top.next = self.top
            self.top = new_top
        else:
            self.top = StackNode(val, val)

    def min(self):
        if not self.top:
            return
        return self.top.min


class StackNode(Node):
    def __init__(self, val, minimum):
        self.val = val
        self.min = minimum
        super(StackNode, self).__init__(val)


# OR

class StackWithMin2(Stack):
    def __init__(self):
        super(StackWithMin2, self).__init__()
        self.stack_of_min = Stack()

    def push(self, val):
        if val <= self.stack_of_min.peek() or self.stack_of_min.is_empty():
            self.stack_of_min.push(val)
        super(StackWithMin2, self).push(val)

    def pop(self):
        if self.top.val == self.stack_of_min.peek():
            self.stack_of_min.pop()
        return super(StackWithMin2, self).pop()

    def min(self):
        return self.stack_of_min.peek()


# Tests

@pytest.mark.parametrize("impl", [StackWithMin, StackWithMin2])
def test_stack_with_min(impl):
    s = impl()
    push_to_stack(s)
    assert s.min() == 3
    s.pop()
    assert s.min() == 3
    s.pop()
    assert s.min() == 7
    s.pop()
    assert s.min() == 8
    s.pop()
    assert not s.min()


def push_to_stack(s):
    s.push(8)
    s.push(7)
    s.push(3)
    s.push(4)
