# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        #swap the children
        #store the left variable in a temporary variable
        tmp = root.left
        #replace left with right
        root.left = root.right
        root.right =tmp

        #invert the sub tree
        #left and right sub tree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        