class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def set_left(self, value):
        self.left = value

    def set_right(self, value):
        self.right = value

class BinarySearchTree():
    
    def __init__(self, node) -> None:
        self.root = node
    
    def insert(self, value, current=None):
        
        if current is None:
            if not self.root:
                self.root = Node(value)
                return
            current = self.root
        if value < current.data:
            if current.left is None:
                current.left = Node(value)
            self.insert(value, current.left)
        if value > current.data:
            if current.right is None:
                current.right = Node(value)
            self.insert(value, current.right)

    def search(self, value, current=None):

        if current is None:
            return False
        
        if value == current.data:
            return True
        if value < current.data:
            return self.search(value, current.left)
        
        
        return self.search(value, current.right)

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

if __name__ == "__main__":
    binary_tree = BinarySearchTree(Node(10))
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.in_order(binary_tree.root)
    print(binary_tree.search(3, binary_tree.root))
    print(binary_tree.search(6, binary_tree.root))
    print(binary_tree.search(7, binary_tree.root))