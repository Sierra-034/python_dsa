
class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    @classmethod
    def inorder(cls, root):
        if root:
            cls.inorder(root.left)
            print(root.value, end=' ')
            cls.inorder(root.right)

    def insert(self, value):
        new_node = TNode(value)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        return self

                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = new_node
                        return self

                    current_node = current_node.right
