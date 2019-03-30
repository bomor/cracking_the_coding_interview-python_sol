from node import create_list


# NOTE: If the node is the last node - it will not be deleted!
def delete_node(n):
    if not n or not n.next:
        return False
    n.val = n.next.val
    n.next = n.next.next
    return True


# Tests

def test_delete_node():
    n = create_list()
    delete_node(n.next)
    assert n.val == 1
    assert n.next.val == 1
    assert n.next.next.val == 4
