# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        st = []
        
        def inOrder(root,st):
            
            if root == None:
                return st 
            if root.left:
                st =  inOrder(root.left,st)
            st.append(root)
            if root.right:
                st = inOrder(root.right,st)
            return st
        def balanceTree(st):
            # print(st)
            if len(st)<=0:
                return None
            rt = st[len(st)//2]
            rt.left = balanceTree(st[:len(st)//2])
            rt.right = balanceTree(st[len(st)//2 +1 : ])
            return rt
        
        st = inOrder(root,st)
        # print(st)
        return balanceTree(st)
        