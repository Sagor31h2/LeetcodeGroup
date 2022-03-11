""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def inorders(root,l):
    
    if root.left:
        inorders(root.left,l)
    l.append(root.data)
    if root.right:
        inorders(root.right,l)
    


def check_binary_search_tree_(root):
    
    l = []
    inorders(root,l)
    # print(l)
    # print(k)
    for i in range(len(l)-2):
        if(l[i] >= l[i+1]):
            return False
    return True
       