class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def insert(root, value):

    if value < root.data:
        if not root.left:
            root.left = Node(value)
        insert(root.left, value)
    if value > root.data:
        if not root.right:
            root.right = Node(value)
        insert(root.right, value)
    
def search(value, current=None):

    if current is None:
        return False

    if value == current.data:
        return True
    
    if value < current.data:
        return search(value, current.left)
    return search(value, current.right)


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)

if __name__ == "__main__":
    root = None
    root = Node(10)
    insert(root, 5)
    insert(root, 3)
    insert(root, 6)
    in_order(root)
    print()
    print(search(5, root))
    print(search(6, root))
    