# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(root):
            if root:

                if root.val < high and root.val > low:
                    self.s += root.val
                if root.left:
                    traverse(root.left)
                if root.right:
                    traverse(root.right)

        self.s = low+high
        traverse(root)
        return self.s
