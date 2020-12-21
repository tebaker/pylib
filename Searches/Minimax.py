class Node:
    def __init__(self, key):
        self.right = None
        self.left  = None
        self.val   = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        ''' Add to exclude duplicates:
                if root.val == key: return root '''
        if key > root.val:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

root = Node(50)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 70)
root = insert(root, 80)

inorder(root)