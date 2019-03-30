from tree_node import TreeNode


# NOTE: contains func visits each node in the small tree at most once,
# and is called no more than once per node of the large tree.
# Worse case runtime is at most O(n*m) (n = size(t1), m = size(t2)).
# If k is the number of occurrences of t2's root in t1, the worst case runtime
# can be characterized as O(n + k*m) 

def is_sub_tree(t1, t2):
    if not t1:
        return False
    elif contains(t1, t2):
        return True
    return is_sub_tree(t1.left, t2) or is_sub_tree(t1.right, t2)


def contains(t1, t2):
    if t2 is None:
        return True
    if t1.val != t2.val:
        return False
    return contains(t1.left, t2.left) and contains(t1.right, t1.right)


# Tests

def test_is_sub_tree():
    t1 = make_big_tree()
    t2 = make_small_tree()
    t3 = make_different_tree()
    assert is_sub_tree(t1, t2)
    assert not is_sub_tree(t1, t3)
    assert is_sub_tree(t1, TreeNode(10))
    assert is_sub_tree(t1, None)
    assert not is_sub_tree(t1, TreeNode(1000))


def make_big_tree():
    t = TreeNode(20)
    t.left = TreeNode(9)
    t.left.left = TreeNode(8)
    t.left.right = TreeNode(10)
    t.left.right.right = TreeNode(15)
    t.right = TreeNode(30)
    return t


def make_small_tree():
    t = TreeNode(9)
    t.left = TreeNode(8)
    t.right = TreeNode(10)
    t.right.right = TreeNode(15)
    return t


def make_different_tree():
    t = TreeNode(9)
    t.left = TreeNode(10)
    t.right = TreeNode(100)
    t.right.right = TreeNode(150)
    return t
