
class Node:
    def __init__(self,key):
        self.data = key 
        self.left = None 
        self.right = None 
    
   

    def InorderTraverse(self):
        if self.left:
            self.left.InorderTraverse()
        print(self.data)
        if self.right: 
            self.right.InorderTraverse()

def takeinput(node):
    
    l = input()
    if l != "":
        node.left = Node(l)
        takeinput(node.left)
    r = input() 
    if r != "":
        node.right = Node(r)
        takeinput(node.right)
    
def preOrder(node):
    print(node.data)
    if node.left:
        preOrder(node.left)
    if node.right:
        preOrder(node.right)

def postOrder(node):
    if node.left:
        postOrder(node.left)
    if node.right:
        postOrder(node.right)
    print(node.data)

def length(root):
    if root == None: 
        return 0
    return max(length(root.left), length(root.right)) + 1


    

if __name__ == "__main__":
    
    # root = Node(1)
    # root.left = Node(2) 
    # root.right = Node(3) 
    # root.left.left = Node(4) 
    # root.left.right = Node(5) 
    # root.left.right.left = Node(6) 
    # root.left.right.right = Node(7)

    # [1, 2, None, ]
    # # root.InorderTraverse()
    # # preOrder(root)
    # # postOrder(root)
    # print(length(root))

    # a = input()
    # if a== "": 
    #     print(None)
    # print(type(a))
    rval = input()
    if rval != "":
        root = Node(rval) 
        takeinput(root)
    else:
        root = Node(None)
    preOrder(root)
