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
        
        pre = []
        # print(q)
        while len(q):
            pre = [n for n in q]
            
            # print([n.val for n in pre])
            for i in range(len(q)):
                n= q.pop(0)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            print([n.val for n in pre])
                
        sm = 0
        # print(pre)
        for n in pre:
            sm+= n.val
        return sm
        
        # print(q)
        