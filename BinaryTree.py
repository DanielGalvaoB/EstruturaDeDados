class BinaryTreeNode:
    def __init__(self, v, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r

class BinaryTree:
    def __init__(self):
        self._root = None

    def insert(self, value):
        if self._root is None:
            self._root = BinaryTreeNode(value)
        else:
            self._insert_recursive(self._root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = BinaryTreeNode(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = BinaryTreeNode(value)
            else:
                self._insert_recursive(current.right, value)



    def update_tree(self, node):
        if node is None:
            return 0

        left_sum = self.update_tree(node.left)
        right_sum = self.update_tree(node.right)

        current_value = node.value
        node.value = left_sum + right_sum

        return node.value + current_value

    def mostrar_arvore(self, node, nivel=0, lado="Raiz"):
        if node is not None:
            print("  " * nivel + f"{lado}: {no.valor}")
            self.mostrar_arvore(node.left, nivel + 1, "Esq")
            self.mostrar_arvore(node.right, nivel + 1, "Dir")

    def inorder_transversal(self, node):
        if node is not None:
            self.inorder_transversal(node.left)
            print(node.value, end=" ")
            self.inorder_transversal(node.right)

valores = list(map(int, input("Digite os valores da árvore separados por espaço: ").split()))
# valores = [4, 2, 1, 3, 5, 6 , 7 , 8]

arvore = BinaryTree()
for v in valores:
    arvore.insert(v)


arvore.inorder_transversal(arvore._root)

print("\n")
arvore.update_tree(arvore._root)
print("\n")
arvore.mostrar_arvore(arvore._root)
