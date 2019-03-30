from chapter2.node import Node
from tree_node import TreeNode


# NOTE: You can easily change the type of the return array to linked list

def list_of_nodes(t):
    final_list = []
    current_level_list = Node(t)
    while current_level_list:
        final_list.append(current_level_list)
        previous_level_node = current_level_list
        current_level_list = None
        while previous_level_node:
            if previous_level_node.val.left:
                if not current_level_list:
                    current_level_list = Node(previous_level_node.val.left)
                else:
                    current_level_list.append_to_tail(previous_level_node.val.left)
            if previous_level_node.val.right:
                if not current_level_list:
                    current_level_list = Node(previous_level_node.val.right)
                else:
                    current_level_list.append_to_tail(previous_level_node.val.right)
            previous_level_node = previous_level_node.next
    return final_list


# Tests

def test_list_of_nodes():
    t = make_tree()
    l = list_of_nodes(t)
    assert l[0].val == t
    assert l[1].val == t.left
    assert l[1].next.val == t.right
    assert l[2].val == t.left.left
    assert l[2].next.val == t.right.right


def make_tree():
    t = TreeNode(0)
    t.right = TreeNode(1)
    t.right.right = TreeNode(2)
    t.right.right.right = TreeNode(3)
    t.left = TreeNode(-1)
    t.left.left = TreeNode(-2)
    t.left.left.left = TreeNode(-3)
    return t
