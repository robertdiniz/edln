class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def insert(root, value):

    if value < root.data:
        if not root.left:
            root.left = Node(value)
        else:
            insert(root.left, value)
    if value > root.data:
        if not root.right:
            root.right = Node(value)
        else:
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

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def del_node(root, key):

    if root is None:
        return root

    if key < root.data:
        root.left = del_node(root.left, key)
    if key > root.data:
        root.right = del_node(root.right, key)

    if key == root.data:
        # caso 1 - o nó atual é uma folha
        if root.left is None and root.right is None:
            return None

        # caso 2 - o nó possui filho esquerdo ou direito
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # caso 3 - possui 2 filhos, percorre o sucessor
        current = root.right
        while(current.left is not None):
            current = current.left
        root.data = current.data
        root.right = del_node(root.right, current.data)

    return root


def size(node):
    if node is None:
        return 0
    hleft = size(node.left)
    hright = size(node.right)
    return hleft + hright + 1


def pre_order(node):
    if node is None:
        return
    
    print(node.data, end=" ")

    pre_order(node.left)
    pre_order(node.right)

def post_order(node):
    if node is None:
        return
    
    post_order(node.left)
    post_order(node.right)

    print(node.data, end=" ")


if __name__ == "__main__":
    root = None
    root = Node(10)
    insert(root, 5)
    insert(root, 1)
    insert(root, 3)
    insert(root, 14)
    insert(root, 12)
    insert(root, 16)
    in_order(root)
    print()
    pre_order(root)
    print()
    post_order(root)
    print()

    # print(search(5, root))
    # print(search(6, root))
    # print(leaves(root))
    # print(count_leaves(root))

    print()

    root = del_node(root, 5)
    in_order(root)
    print()

    print(count_leaves(root))
    print(size(root))


    # del_node(root, 3)
    # in_order(root)
    # print()
    # del_node(root, 5)
    # in_order(root)