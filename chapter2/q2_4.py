from node import Node


def add_lists(l1, l2, carry):
    if not l1 and not l2:
        if not carry:
            return
        else:
            return Node(carry)
    else:
        if not l1:
            total = l2.val + carry
        elif not l2:
            total = l1.val + carry
        else:
            total = l1.val + l2.val + carry
    result_node = Node(total % 10)
    n = add_lists(l1.next if l1 else None, l2.next if l2 else None, total / 10)
    result_node.next = n
    return result_node


# Tests

def test_add_lists():
    l1 = Node(3)
    l1.append_to_tail(1)
    l1.append_to_tail(5)
    l2 = Node(5)
    l2.append_to_tail(9)
    l2.append_to_tail(2)
    l3 = add_lists(l1, l2, 0)
    assert l3.val == 8
    assert l3.next.val == 0
    assert l3.next.next.val == 8
