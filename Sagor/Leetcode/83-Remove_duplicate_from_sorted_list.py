from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = temp = head
        while (temp and temp.next):
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return c


if __name__ == "__main__":
    one = ListNode(1)
    two = ListNode(1)
    three = ListNode(2)

    head = one
    one.next = two
    two.next = three

    s = Solution()
    x = (s.deleteDuplicates(head))
    while x:
        print(x.val)
        x = x.next
