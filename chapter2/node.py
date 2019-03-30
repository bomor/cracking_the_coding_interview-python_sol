class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val

    def append_to_tail(self, val):
        new_node = Node(val)
        n = self
        while n.next is not None:
            n = n.next
        n.next = new_node


def delete_node(head, val):
    if head.val == val:
        return head.next
    node = head
    while node.next is not None:
        if node.next.val == val:
            node.next = node.next.next
            return head
        node = node.next
    return head


def create_list():
    n = Node(1)
    n.append_to_tail(3)
    n.append_to_tail(1)
    n.append_to_tail(4)
    n.append_to_tail(3)
    return n
