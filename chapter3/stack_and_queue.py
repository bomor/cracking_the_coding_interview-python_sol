from chapter2.node import Node


class Stack(object):
    def __init__(self):
        self.top = None

    def pop(self):
        if not self.top:
            return None
        val = self.top.val
        self.top = self.top.next
        return val

    def push(self, val):
        new_top = Node(val)
        new_top.next = self.top
        self.top = new_top

    def peek(self):
        if not self.top:
            return None
        return self.top.val

    def is_empty(self):
        return self.top is None


class Queue(object):
    def __init__(self):
        self.last = None
        self.first = None

    def enqueue(self, val):
        new_last = Node(val)
        if not self.first:
            self.last = new_last
            self.first = self.last
        else:
            self.last.next = new_last
            self.last = self.last.next

    def dequeue(self):
        if not self.first:
            return None
        val = self.first.val
        self.first = self.first.next
        return val
