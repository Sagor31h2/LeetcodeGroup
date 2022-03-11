

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
    LCA = None 
    temp = root 
    while temp:
        if(v1< temp.info and v2<temp.info):
            LCA = temp 
            temp = temp.left 
        elif(v1> temp.info and v2>temp.info):
            LCA = temp
            temp = temp.right
        else: 
            LCA = temp 
            return LCA 
    return LCA 
