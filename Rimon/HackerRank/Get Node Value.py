

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    # Write your code here
    temp = llist 
    prev = None 
    while temp:
        nxt = temp.next 
        temp.next = prev
        prev = temp 
        temp = nxt 
    
    pos = positionFromTail
    while pos:
        prev = prev.next 
        pos-=1 
    return prev.data
        
    
