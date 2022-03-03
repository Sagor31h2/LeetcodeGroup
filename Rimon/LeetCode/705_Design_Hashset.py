class MyHashSet:

    def __init__(self):
        self.head = ListNode()

    def add(self, key: int) -> None:
        temp = self.head 
        while temp.next:
            # print(temp.val)
            if temp.val == key: 
                return None
            temp = temp.next
        
        # print("added ", key)
        if temp.val == key:
            return None
        temp.next = ListNode(key)
        # print(self.head)
        

    def remove(self, key: int) -> None:
        temp = self.head
        while temp.next:
            if temp.next.val == key:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
            
    def contains(self, key: int) -> bool:
        print("contains:", self.head)
        temp = self.head.next
        while temp: 
            if temp.val == key:
                return True
            temp = temp.next
        return False 
            

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)