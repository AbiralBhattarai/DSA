class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.right = right
        self.left = left

    def addNode(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.addNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.addNode(data)
            else:
                self.data = data
    
    def inorderTr(self):
        if self.left :
            self.left.inorderTr()
        print(self.data)
        if self.right:
            self.right.inorderTr()
    def postorderTr(self):
        if self.left :
            self.left.postorderTr()
        if self.right:
            self.right.postorderTr()
        print(self.data)    
    def preorderTr(self):
        print(self.data)
        if self.left :
            self.left.preorderTr()
        if self.right:
            self.right.preorderTr()

    def search(self,value):
        if value < self.data:
            if self.left:
                if self.left.data:
                    return self.left.search(value)
        if value > self.data:
            if self.right:
                if self.right.data:
                    return self.right.search(value)
        else: 
            return False
    def get_min(self):
        if self.left is None:
            return self.data
        return self.left.get_min()
    
    def get_max(self):
        if self.right is None:
            return self.data
        return self.right.get_min()

    def delete(self,value):
        def min_value(self):
            if self.left is None:
                return self.data
            return self.left.min_value()
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None:
                curr = self.right
                curr = None
                return curr
            elif self.right is None:
                curr = self.left
                curr = None
                return curr

            curr = min_value(self.right)
            self.data = curr
            self.right = self.right.delete(value)
        return self 

obj = Node(50)
obj.addNode(40)
obj.addNode(60)
obj.addNode(30)
obj.addNode(45)
obj.delete(50)
obj.inorderTr()
print("\n")
obj.preorderTr()
print("\n")
obj.postorderTr()
print("\n")
print(obj.get_max())
print("\n")
print(obj.get_min())