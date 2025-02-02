class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# insert
def insert(root, key):

    if root is None:
        return Node(key)

    if root.data == key:
        return root
    
    # se o novo valor for maior que a raiz
    if root.data < key:
        if not root.right:
            root.right = Node(key)
        root.right = insert(root.right, key)
    else:
        if not root.left:
            root.left = Node(key)
        root.left = insert(root.left, key)
    
    return root
                
# search
def search(root, key):

    if root is None:
        return False
    
    if root.data == key:
        return True
    
    if root.data < key:
        return search(root.right, key)
    
    return search(root.left, key)

# remove
def remove_node(root, key):
    
    if root is None:
        return root

    if key < root.data:
        root.left = remove_node(root.left, key)
    if key > root.data:
        root.right = remove_node(root.right, key)
    
    if key == root.data:

        # caso 1 - se for uma folha, apenas remova.
        if root.left is None and root.right is None:
            return None
    
        # caso 2 - o nó possui um filho esquerdo ou direito
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        # caso 3 - o nó possui 2 filhos
        current = root.right
        while(current.left is not None):
            current = current.left
        root.data = current.data
        root.right = remove_node(root.right, current.data)

    return root


# count_leaves
# del_node
# size

# in_order
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)

# pre_order
def pre_order(root):
    if root:
        print(root.data, end=" ")
        pre_order(root.left)
        pre_order(root.right)

# pos_order
def pos_order(root):
    if root:
        pos_order(root.left)
        pos_order(root.right)
        print(root.data, end=" ")

if __name__ == "__main__":

    root = Node(50)
    insert(root, 20)
    insert(root, 30)
    insert(root, 10)
    insert(root, 40)
    insert(root, 60)
    insert(root, 70)
    in_order(root)
    print()
    print(search(root, 30))
    remove_node(root, 50)
    pre_order(root)