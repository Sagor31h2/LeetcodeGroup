

#
# Complete the 'reversePrint' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversePrint(llist):
    # Write your code here
    temp = llist 
    prev = None 
    while temp:
        next = temp.next 
        temp.next = prev
        prev = temp
        temp = next 
    temp = prev 
    while temp:
        print(temp.data)
        temp = temp.next
    
