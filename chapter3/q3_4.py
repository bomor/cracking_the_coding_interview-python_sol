import pytest
from stack_and_queue import Stack

def move_disks(n, source, buff, dest):
	if n > 0:
		move_disks(n-1, source, dest, buff)
		dest.push(source.pop())
		move_disks(n-1, buff, source, dest)
		
############## Tests ##############

def test_move_disks():
	source = Stack()
	push_to_stack(source)
	buff = Stack()
	dest = Stack()
	move_disks(5, source, buff, dest)
	for i in xrange(1,5):
		assert dest.pop() == i

def push_to_stack(s):
	s.push(5)
	s.push(4)
	s.push(3)
	s.push(2)
	s.push(1)