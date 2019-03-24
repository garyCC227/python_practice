'''
Binary search tree

traversal in BST：
1. in order traversal： 从小到大
2. pre-order traversal: 先root node， 然后left SUBTREE， 然后right SUBTREE，recursively!
    (是subtree哦！！)
3. post-order traversal: 先left subtree， 然后right subtree， 然后root, recursively! (是subtree哦)

'''




class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return " {},".format(self.data)

class BST(object):
    def __init__(self):
        self.root = None

    def remove(self, data):
        '''
        for remove in a BST:
            - leaf -> easy
            - single successor -> easy
            - two successors:
                - find the predecessor(the largest one in left subtree)
                - then swap the predecessor and root node -> how easy !! so forget about
                    find the smallest one in right sub-tree!!
        '''
        if self.root:
            return self.remove_node(data, self.root)

    def remove_node(self, data, node):
        #this data is not in BST
        if not node:
            return node

        if data > node.data:
            node.rightChild = self.remove_node(data, node.rightChild)
        elif data < node.data:
            node.leftChild = self.remove_node(data, node.leftChild)
        else:
            #remove a left
            if not node.leftChild and not node.rightChild:
                del node
                return None
            #single left child or right child
            elif not node.leftChild:
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                return tempNode
            else:
                # the node has two succesor
                tempNode = self.get_predeccor(node.leftChild)
                node.data = tempNode.data
                node.leftChild = self.remove_node(tempNode.data, node.leftChild)
        return node

    def get_predeccor(self, node):
        if node.rightChild:
            return self.get_predeccor(node.rightChild)
        return node

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    @property
    def min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return node.data

    @property
    def max_value(self):
        if self.root:
            return self.get_max(self.root)

    def traversal(self):
        if self.root:
            return self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        if node.leftChild:
            self.in_order_traversal(node.leftChild)

        print(node, end="")

        if node.rightChild:
            self.in_order_traversal(node.rightChild)



if __name__ == '__main__':
    bst = BST()
    bst.insert(6)
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(7)
    bst.insert(8)
    bst.insert(1)
    bst.traversal()
    print("")
    print(bst.root.data)
    print(bst.max_value)
    print(bst.min_value)
    bst.remove(1)
    bst.traversal()
