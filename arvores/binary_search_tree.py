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

def count_sheets(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_sheets(node.left) + count_sheets(node.right)

def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def del_node(root, key):

    if root is None:
        return root

    if key < root.data:
        root.left = del_node(root.left, key)
    if key > root.data:
        root.right = del_node(root.right, key)

    if key == root.data:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)
        
    return root


def size(node):
    if node is None:
        return 0
    hleft = size(node.left)
    hright = size(node.right)
    return hleft + hright + 1


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
    print(size(root))
    print(count_sheets(root))