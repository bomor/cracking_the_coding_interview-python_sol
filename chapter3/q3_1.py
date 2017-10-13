from stack_and_queue import Stack
import pytest

# In this approach, any stack can grow as long as there is any
# free space in the array.
# NOTE: We face a problem of unused space - if a stack deletes
# some of its elements, we would not be able to use those newly freed spaces.

class ThreeStacks(object):

	def __init__(self, stack_size):
		self.arr = [None] * (3 * stack_size)
		self.indices = [-1, -1, -1]
		self.current_index = 0
	
	def push(self, stack_id, val):
		if self.current_index >= len(self.arr):
			return False
		new_val = StackNode(self.indices[stack_id], val)
		self.arr[self.current_index] = new_val
		self.indices[stack_id] = self.current_index
		self.current_index +=1
		return True

	def pop(self, stack_id):
		if self.is_empty(stack_id):
			return None
		n_to_pop = self.arr[self.indices[stack_id]]
		val = n_to_pop.val
		previous_index = n_to_pop.previous_index
		self.arr[self.indices[stack_id]] = None
		self.indices[stack_id] = previous_index
		return val
	
	def peek(self, stack_id):
		return self.arr[self.indices[stack_id]].val

	def is_empty(self, stack_id):
		return self.indices[stack_id] == -1

class StackNode(object):
	def __init__(self, previous_index, val):
		self.previous_index = previous_index
		self.val = val

# OR
# In this approach, elements of stack <n> stored at i%3 == n indices in the main array.
# The main array grows as long as needed by one of the stacks
# NOTE: This approach can be optimized by adding "clean the array" func while pop.
# (If the arr contains [None, None, None] by the end of it)


class ThreeStacks2(object):
	def __init__(self):
		self.indices = [-3, -2, -1]
		self.arr = []
		
	def push(self, stack_id, val):
		self.indices[stack_id] += 3
		if self.indices[stack_id] >= len(self.arr):
			self.arr = self.arr + [None]*3
		self.arr[self.indices[stack_id]] = val

	def pop(self, stack_id):
		if self.is_empty(stack_id):
			return False
		val = self.arr[self.indices[stack_id]] 
		self.arr[self.indices[stack_id]] = None
		self.indices[stack_id] -= 3
		return val
		
	def peek(self, stack_id):
		if is_empty(stack_id):
			return False
		return self.arr[self.indices[stack_id]]
	
	def is_empty(self, stack_id):
		return self.indices[stack_id] < 0
	
@pytest.mark.parametrize("impl", [ThreeStacks(10), ThreeStacks2()])		
def test_three_stacks(impl):
	s1 = stack1()
	s2 = stack2()
	s3 = stack3()	
	s1s2s3 = impl
	push_to_s1s2s3(s1s2s3)
	assert s1s2s3.pop(0) == 1
	assert s1s2s3.pop(0) == 0
	assert s1s2s3.pop(1) == 3
	assert s1s2s3.pop(1) == 2
	assert s1s2s3.pop(2) == 5
	assert s1s2s3.pop(2) == 4
	assert not s1s2s3.pop(0)


def push_to_s1s2s3(s1s2s3):
	s1s2s3.push(0,0)
	s1s2s3.push(1,2)
	s1s2s3.push(2,4)
	s1s2s3.push(0,1)
	s1s2s3.push(1,3)
	s1s2s3.push(2,5)

def stack1():
	s = Stack()
	s.push(0)
	s.push(1)


def stack2():
	s = Stack()
	s.push(2)
	s.push(3)


def stack3():
	s = Stack()
	s.push(4)
	s.push(5)
