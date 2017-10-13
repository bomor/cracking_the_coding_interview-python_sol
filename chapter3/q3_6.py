from stack_and_queue import Stack

# NOTE: If you want to make an "in place" sort (instead of returning a new stack)
# just change the WHILE condition to  << val >= buff.peek() and not buff.is_empty() >>.
# Then, at the end of the func, pop all elements from buff and push to s (one by one).

def sort_stack(s):
	buff = Stack()
	while not s.is_empty():
		val = s.pop()
		while val < buff.peek() and not buff.is_empty():
			s.push(buff.pop())
		buff.push(val)
	return buff

############## Tests ##############	

def test_sort_stack():
	s = Stack()
	push_to_stack(s)
	s = sort_stack(s)
	assert s.pop() == 7
	assert s.pop() == 4
	assert s.pop() == 2
	assert s.pop() == 1
	assert not s.pop()
	
def push_to_stack(s):
	s.push(2)
	s.push(7)
	s.push(1)
	s.push(4)