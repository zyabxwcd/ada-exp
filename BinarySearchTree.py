class Node:
    counter = 0

    def __init__(self, info=None):
        self.info = info
        self.left = None
        self.right = None

    def set_value(self, info):
        self.info = info

    def insert(self, info):
        if self.info is None:
            self.set_value(info)
        else:
            if info < self.info:
                if self.left is None:
                    self.left = Node(info)
                else:
                    self.left.insert(info)
            else:
                if self.right is None:
                    self.right = Node(info)
                else:
                    self.right.insert(info)

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.info, end=' ')
        if self.right is not None:
            self.right.print_tree()

    def search(self, value):
        Node.counter += 1
        if self.info is None:
            return False
        elif self.info == value:
            return True
        else:
            if value < self.info:
                if self.left is None:
                    return False
                else:
                    return self.left.search(value)
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.search(value)

# Driver Code
elements = [int(i) for i in input('Enter elements : ').split()]

choice = True
root = Node()

for element in elements:
    root.insert(element)

print('Tree : ', end='')
root.print_tree()

while(choice):
    value = int(input('\nEnter element to search : '))
    
    if root.search(value):
        print('Element found in {} iteration(s)'.format(root.counter))
        root.counter = 0
    else:
        print('Element not found.')
        root.counter = 0

    choice = input('Search element ? (y/n) ')
    choice = True if choice == 'y' else False