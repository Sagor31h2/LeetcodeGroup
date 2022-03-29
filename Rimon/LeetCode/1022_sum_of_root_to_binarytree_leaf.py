# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        st = []
        sm = 0 
        def decode(st):
            var =0 
            for i in range(len(st)):
                var += st[i] * 2 ** (len(st)-i-1)
            return var
        def preOrder(root,st,sm):
            # print(sm)
            if root.left == None and root.right == None:
                st.append(root.val)
                sm += decode(st)
                print(st)
                st.pop()
                return sm
                
            st.append(root.val)
            if root.left:
                sm = preOrder(root.left,st,sm)
            if root.right:
                sm = preOrder(root.right,st,sm)
            st.pop()
            return sm
            
        sm = preOrder(root,st,sm)
        return sm