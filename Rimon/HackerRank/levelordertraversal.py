

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    q = []
    q.append(root)
    while q:
        n = q[0]
        print(n.info,end=" ")
         
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
        q.pop(0) 
        
