#Binary Tree DFS
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        current = self.root
        while True:
            if value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
            elif value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                current.value = value
                break

    def DFSTree(self, node: Node):
        if node is None:
            return
        else:
            print(node.value, end = ' ')
        self.DFSTree(node.left)
        self.DFSTree(node.right)

    def PrintDFSTree(self):
        self.DFSTree(self.root)

def main():
    root = Tree(7)
    root.insert(2)
    root.insert(25)
    root.insert(9)
    root.insert(80)
    root.insert(0)
    root.insert(5)
    root.insert(15)
    root.insert(8)
    
    root.PrintDFSTree()
main()