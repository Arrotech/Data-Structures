class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)

        else:
            self.data = data

    def in_order_traversal(self, root):
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.data)
            res = res + self.in_order_traversal(root.right)
        return res

    def pre_order_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.data)
        return res

    def find_value(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " Not Found(:"
            else:
                return self.left.find_value(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " Not Found(:"
            else:
                return self.right.find_value(value)
        else:
            return str(value) + " Okay"

    # Breadth first search
    def level_order_traversal(self, root):
        if root is None:
            return

        queue = []
        queue.append(root)
        data = []

        while (len(queue) > 0):
            node = queue.pop(0)
            data.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        print(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()



if __name__ == '__main__':
    root = Node(12)
    root.insert_node(6)
    root.insert_node(14)
    root.insert_node(3)
    root.print_tree()
    print(root.in_order_traversal(root))
    print(root.pre_order_traversal(root))
    print(root.post_order_traversal(root))
    print(root.find_value(14))
    print(root.find_value(1))
    root.level_order_traversal(root)