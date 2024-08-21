class Node:
    def __init__(self,data):
        self.left = None
        self.right = None 
        self.data = data

    def insert(self,data):
        if self.data is None:
            self.data = data

        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


if __name__ == '__main__':
    root = Node(5)
    root.insert(1)
    root.insert(3)
    root.insert(6)
    root.insert(7)
    root.insert(8)
    root.insert(9)
    root.insert(2)

#Printing all nodes 

# PreOrder Traversal
def PreOrder(node):
    if node is None:
        return
    else:
        print(node.data,end = ' ')
        PreOrder(node.left)
        PreOrder(node.right)

print("PreOrder : ")
PreOrder(root)
print("")

#InOrder Traversal
def InOrder(node):
    if node is None:
        return
    else:
        InOrder(node.left)
        print(node.data, end= ' ')
        InOrder(node.right)


print("InOrder : ")
InOrder(root)
print("")

#postOrder Traversal
def postOrder(node):
    if node is None:
        return
    else:
        postOrder(node.left)
        
        postOrder(node.right)
        print(node.data,end = ' ')


print("postOrder : ")
postOrder(root)







