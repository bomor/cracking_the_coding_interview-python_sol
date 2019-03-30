from tree_node import TreeNode


def minimal_height_tree(arr):
    if not arr:
        return None
    root_index = len(arr) / 2
    root = TreeNode(arr[root_index])
    root.left = minimal_height_tree(arr[:root_index])
    root.right = minimal_height_tree(arr[root_index + 1:])
    return root


# Tests

def test_minimal_height_tree():
    arr = [1, 2, 100, 200, 201, 300]
    t = minimal_height_tree(arr)
    assert t.val == 200
    assert t.right.val == 300
    assert t.right.left.val == 201
    assert t.left.val == 2
    assert t.left.right.val == 100
    assert t.left.left.val == 1
