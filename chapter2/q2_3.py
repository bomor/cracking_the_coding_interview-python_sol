from node import Node, create_list
# 2.3
# NOTE: If the node is the last node - it will not be deleted!

def delete_node(n):
	if not n.next or not n:
		return False 
	n.val = n.next.val 
	n.next = n.next.next
	return True	

############## Tests ##############

def test_delete_node():
	n = create_list()
	delete_node(n.next)
	assert n.val == 1
	assert n.next.val == 1
	assert n.next.next.val == 4