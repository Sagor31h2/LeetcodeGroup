

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    q = [(root,0)]
    pos = 0
    mp = dict()
    #
    mp[pos] = root
    while q: 
        f,pos = q.pop(0)
        
        if  not pos in mp:
            mp[pos] = f 
        if f.left:
            q.append((f.left,pos-1))
        if f.right:
            q.append((f.right,pos+1))
    
    for i in sorted(mp.keys()):
        print(mp[i],end=" ")
        
