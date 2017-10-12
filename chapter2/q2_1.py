from node import Node, create_list
# 2.1
# (An additional set is needed)

def delete_dups(n):
	list_vals = set()
	previous = Node(None)
	while n != None:
		if n.val in list_vals:
			previous.next = n.next

		else:
			list_vals.add(n.val)
			previous = n
		n = n.next
		print list_vals
		
# OR (Without an additional buffer)

def delete_dups2(head):
	current = head
	while current != None:
		runner = current.next
		previous = current
		while runner != None:
			if current.val == runner.val:
				previous.next = runner.next
			else:
				previous = previous.next
			runner = runner.next
		current = current.next
		
############## Tests ##############

def test_delete_dups():
	n = create_list()
	delete_dups(n)
	assert n.val == 1
	assert n.next.val == 3
	assert n.next.next.val == 4
	assert n.next.next.next == None

def test_delete_dups2():
	n = create_list()
	delete_dups(n)
	assert n.val == 1
	assert n.next.val == 3
	assert n.next.next.val == 4
	assert n.next.next.next == None