#create a  Node
import collections
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None
    # Isert Node
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

### BFS Starts
#Adjacency List to keep each parent and child node in dictionary a pair of lists

def makeList(r):
    if r is None:
        return
    else:
        d[r.data] = []
        makeList(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        if r.right:
            d[r.data].append(r.right.data)
        makeList(r.right)    
    return d    

#BFS Code also called level order traversal
def bfs(al):
    queue = collections.deque('g') #g is root element passed as default

    visited = []

    #iterate queue
    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
    print(visited)    



if __name__ == '__main__':
# Insert Data
# create a root node
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')

    d = {}
    # creating and calling adjacency list
    aList = makeList(root)
    print(aList)
    bfs(aList)
print("Inorder : ")
#Inorder Traversal
def inorder(node):
    if node is None:
        return
    else:
        inorder(node.left)
        print(node.data,end = ' ')
        inorder(node.right)

inorder(root)

print("PostOrder : ")
def postorder(node):
    if node is None:
        return
    else:
        postorder(node.left)
        
        postorder(node.right)
        print(node.data,end = ' ')

postorder(root)

print("Preorder : ")
def preorder(node):
    if node is None:
        return
    else:
        print(node.data,end = ' ')
        preorder(node.left)
        
        preorder(node.right)

preorder(root)


















        

