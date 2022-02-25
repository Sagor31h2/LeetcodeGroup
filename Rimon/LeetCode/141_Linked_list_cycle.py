# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        temp = head
        # d = ListNode("tmp")
        while temp is not None:
            if temp.val =="tmp":
                return True
            temp.val = "tmp"
            temp = temp.next
        
        return False
            