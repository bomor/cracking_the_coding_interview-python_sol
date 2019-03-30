class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def is_leaf(self):
        return not self.right and not self.left
