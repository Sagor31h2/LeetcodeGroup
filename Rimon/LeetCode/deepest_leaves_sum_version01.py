# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        
        # while len(q):
        #     node = q.pop(0)
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        
        def length(root):
            if root == None:
                return 0;
            return max(length(root.left),length(root.right))+1
        
        ln = length(root)
        # print(ln)
        k = ln-1
        while len(q) and k>0:
            for i in range(len(q)):
                n= q.pop(0)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                
            k-=1
        sm = 0
        for n in q:
            sm+= n.val
        return sm
        
        # print(q)
        