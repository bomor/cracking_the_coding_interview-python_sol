from stack_and_queue import Stack, Queue


class MyQueue(object):
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, val):
        self.s1.push(val)

    def dequeue(self):
        if self.s2.is_empty():
            self.move_all()
        return self.s2.pop()

    def move_all(self):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())


# Tests

def test_my_queue():
    q1 = MyQueue()
    q2 = Queue()
    q1.enqueue(1)
    q2.enqueue(1)
    q1.enqueue(2)
    q2.enqueue(2)
    for i in xrange(3):
        assert q1.dequeue() == q2.dequeue()
    q1.enqueue(1)
    q2.enqueue(1)
    assert q1.dequeue() == q2.dequeue()
