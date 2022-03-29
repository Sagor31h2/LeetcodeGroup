class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def decode(st):
    return
def preOrder(root):
    print(sm)
    if root == None:
        decode(st)
        st.pop()
        return 
    st.append(root.val)
    preOrder(root.left)
    preOrder(root.right)

st = []
sm = 1
root=TreeNode(val=1,left=TreeNode(0), right = TreeNode(2))


preOrder(root)