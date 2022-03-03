

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    # Write your code here
    temp = llist 
    while temp:
        next = temp.next 
        temp.next = temp.prev 
        temp.prev = next 
        llist = temp 
        temp = next 
    return llist 
