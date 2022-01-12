### AVL TREE IMPLEMENTATION
# Definiamo la classe **node**

class node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # percorso più lungo dal nodo considerato a una foglia 


# Definiamo la classe __AVL__
# - Definiamo la funzione __balance()__ per calcolare il fattore di bilancio che serve a definire se un AVL Tree sia o meno bilanciato 
# - Definiamo la funzione __MinimumValueNode()__ usata per trovare il nodo vuoto 
# - Definiamo la funzione __rotateR()__ per ruotare l'albero in senso orario
# - Definiamo la funzione __rotateL()__ per ruotare l'albero in senso anti-orario
# - Definiamo la funzione __insert()__ per inserire un elemento all'interno dell'AVL Tree
# - Definitamo la funzione __preorder()__ per attraversare l'albero seguendo il preordine

class AVL: 
    def height(self, Node):
        if Node is None:
            return 0 
        else: 
            return Node.height
        
    def balance(self, Node):
        if Node is None: 
            return 0 
        else: 
            return self.height(Node.left) - self.height(Node.right)
    
    def MinimumValueNode(self, Node):
        if Node is None or Node.left is None:
            return Node
        else: 
            return self.MinimumValueNode(Node.left)
        
    def rotateR(self, Node):
        a = Node.left
        b = a.right 
        a.right = Node
        Node.left = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a 
    
    def rotateL(self, Node):
        a = Node.right
        b = a.left
        a.left = Node
        Node.right = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a
    
    def insert(self, val, root):
        if root is None:
            return node(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        elif val > root.value:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root
    
    def preorder(self, root):
        if root is None:
            return 
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)


Tree = AVL()
rt = None

rt = Tree.insert(3, rt)
rt = Tree.insert(5, rt)
rt = Tree.insert(7, rt)
Tree.preorder(rt)
rt = Tree.insert(1, rt)
rt = Tree.insert(2, rt)
print("PREORDER")
Tree.preorder(rt)
rt = Tree.insert(4, rt)
rt = Tree.insert(6, rt)
rt = Tree.insert(8, rt)
rt = Tree.insert(9, rt)
print("PREORDER")
Tree.preorder(rt)
