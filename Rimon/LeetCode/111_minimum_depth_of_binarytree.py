# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = []
        q.append(root)
        count = 0
        while len(q)>0:
            count+=1
            l = len(q)
            for i in range(l):
                n = q.pop(0)
                
                if n.left and n.right:
                    q.append(n.left)
                    q.append(n.right)
                elif n.left:
                    q.append(n.left)
                elif n.right:
                    q.append(n.right)
                else:
                    return count
        
        return count 
            