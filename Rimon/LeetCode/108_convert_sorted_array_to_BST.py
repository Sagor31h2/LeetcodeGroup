# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        l = len(nums)
        # print(l)
        v = nums[l//2]
        # print(v)
        root = TreeNode(v)
        
        def insert(root,nums):
            l = len(nums)
            # print(l)
            if(l <=0):
                return
            v = nums[l//2]
            # print(v)
            if v < root.val:
                root.left = TreeNode(v)
                insert(root.left,nums[:l//2])
                insert(root.left,nums[l//2+1:])
            elif v>root.val :
                root.right = TreeNode(v)
                insert(root.right,nums[:l//2])
                insert(root.right,nums[l//2+1:])
            # return root
            
            
        insert(root,nums[:l//2])
        insert(root,nums[l//2+1:])
        
        return root