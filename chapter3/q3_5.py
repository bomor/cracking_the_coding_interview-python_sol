from stack_and_queue import Stack
import pytest

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

############## Tests ##############

def test_my_queue():
	q = MyQueue()
	q.enqueue(1)
	q.enqueue(2)
	assert q.dequeue() == 1
	assert q.dequeue() == 2
	assert not q.dequeue()
	q.enqueue(1)
	assert q.dequeue() == 1
