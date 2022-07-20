import queue
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def inputtree():
    print("Enter the root data")
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=Node(rootdata)
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        curr=q.get()
        print("Enter the leftchild of "+str(curr.data))
        leftdata=int(input())
        if leftdata!=-1:
            leftchild=Node(leftdata)
            curr.left=leftchild
            q.put(leftchild)
        print("Enter the rightchild of "+str(curr.data))
        rightdata=int(input())
        if rightdata!=-1:
            rightchild=Node(rightdata)
            curr.right=rightchild
            q.put(rightchild)
    return root

def printrange(k1,k2,root):
    if root==None:
        return None
    if root.data>k2:
        printrange(k1,k2,root.left)
    elif root.data<k1:
        printrange(k1,k2,root.right)
    else:
        print(root.data)
        printrange(k1,k2,root.left)
        printrange(k1,k2,root.right)
    

def printtree(root):
    if root==None:
        return None
    print(root.data,end=' ')
    if root.left!=None:
        print("L->"+str(root.left.data), end=" ")
              
    if root.right!=None:
              print("R->"+str(root.right.data),end=" ")
    print()
    printtree(root.left)
    printtree(root.right)
root=inputtree()
printrange(5,10,root)

    
