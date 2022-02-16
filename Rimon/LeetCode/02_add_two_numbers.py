# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        d = 0
        head = temp = ListNode()
        while l1 is not None and l2 is not None: 
            total = l1.val + l2.val + d
            r = total % 10
            d = total // 10     
            temp.next = ListNode(r)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        
        if l1 is not None:          #Tried a Different way 
            flg = l1
        else:
            flg = l2
            
        while flg is not None:
            total = flg.val + d
            r = total % 10
            d = total // 10
            temp.next = ListNode(r)
            temp = temp.next
            flg = flg.next
        else:
            if(d>0):
                temp.next = ListNode(d)
        
        # print(head.next)
        return head.next
            
            
        
        
        
            
            
            