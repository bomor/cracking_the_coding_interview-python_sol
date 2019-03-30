from node import create_list


def nth_to_last(head, n):
    if n < 0:
        return
    p1 = head
    p2 = head
    for i in xrange(n):
        # in case that list size < n
        if not p2:
            return
        p2 = p2.next
    while p2.next:
        p1 = p1.next
        p2 = p2.next
    return p1


# Tests

def test_nth_to_last():
    n = create_list()
    assert nth_to_last(n, 4) == n
    assert nth_to_last(n, 3) == n.next
