from tree_node import TreeNode
import pytest

# NOTE: max_depth() and min_depth() does not return the REAL max_depth and min_depth,
# but max_depth + 1 and min_depth + 1. You might think this is a bug, but I found this compromise
# makes the code shorter. Anyway, is_balanced DOES return the real bool (it checks the diff
# between max_depth and min_depth.

def is_balanced(t):
	print max_depth(t)
	print min_depth(t)
	return max_depth(t) - min_depth(t) <= 1

def max_depth(t):
	if not t:
		return 0
	return 1 + max(max_depth(t.left), max_depth(t.right))

def min_depth(t):
	if not t:
		return 0
	return 1 + min(min_depth(t.left), min_depth(t.right))

############## Tests ##############	

def test_is_balanced():
	t1 = not_balanced_tree()
	t2 = balanced_tree()
	assert not is_balanced(t1)
	assert is_balanced(t2)

def not_balanced_tree():
	t = TreeNode(0)
	t.left = TreeNode(2)
	t.right = TreeNode(-1)
	t.left.left = TreeNode(3)
	t.left.left.left = TreeNode(4)
	return t

def balanced_tree():
	t = TreeNode(0)
	t.left = TreeNode(2)
	t.right = TreeNode(-1)
	t.left.left = TreeNode(3)
	t.right.right = TreeNode(-2)
	return t