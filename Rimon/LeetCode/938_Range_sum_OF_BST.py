# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sm = 0 
        
        def travarse(root,low,high,sm):
            if root == None:
                return sm
            if root.val >= low and root.val <= high:
                sm += root.val
            if root.left and root.val > low:
                sm = travarse(root.left,low,high,sm)
            if root.right and root.val < high:
                sm = travarse(root.right,low,high,sm)
            return sm
        
        return travarse(root,low,high,sm)
        

    
