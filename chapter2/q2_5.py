from node import Node


def find_loop_beg(head):
    s = head
    f = head
    # Find the meeting point
    while f.next:
        s = s.next
        f = f.next.next
        if s == f:
            break
    # Check if list has a loop
    if not f.next:
        return
    s = head
    while s != f:
        s = s.next
        f = f.next
    return f


# Tests

def test_find_loop_beg():
    loop_list = create_loop_list()
    assert find_loop_beg(loop_list).val == 4


def create_loop_list():
    n = Node(1)
    n.append_to_tail(2)
    n.append_to_tail(3)
    n.append_to_tail(4)
    n.append_to_tail(5)
    n.append_to_tail(6)
    n.next.next.next.next.next = n.next.next.next
    return n
