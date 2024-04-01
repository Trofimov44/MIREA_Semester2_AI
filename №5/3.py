class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

# Пример использования:
root = Tree(5)
root.insert(3)
root.insert(7)
root.insert(1)
root.insert(4)
root.insert(6)
root.insert(8)

root.PrintTree()
