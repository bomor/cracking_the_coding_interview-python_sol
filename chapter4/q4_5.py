from tree_node import TreeNode


def inorder_succ(n):
    if not n:
        return None
    if n.right:
        return most_left_child(n.right)
    if n.parent.left == n:
        return n.parent
    return go_up(n.parent)


def most_left_child(n):
    while n.left:
        n = n.left
    return n


def go_up(n):
    while n.parent:
        if n.parent.left == n:
            break
        n = n.parent
    return n.parent


class TreeNodeWithParent(TreeNode):
    def __init__(self, val, parent):
        self.parent = parent
        super(TreeNodeWithParent, self).__init__(val)


# Tests

def test_inorder_succ():
    t = make_tree()
    assert inorder_succ(t).val == 11
    assert not inorder_succ(t.right)
    assert inorder_succ(t.left).val == 9
    assert inorder_succ(t.left.left).val == 8
    assert inorder_succ(t.left.right).val == 10


def make_tree():
    t = TreeNodeWithParent(10, None)
    t.right = TreeNodeWithParent(11, t)
    t.left = TreeNodeWithParent(8, t)
    t.left.left = TreeNodeWithParent(7, t.left)
    t.left.right = TreeNodeWithParent(9, t.left)
    return t
