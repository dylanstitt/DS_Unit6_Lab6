# Dylan Stitt
# Unit 6 Lab 6
# Binary Search Tree Delete

class BinarySearchTree:
    class BinaryNode:

        def __init__(self, value, left=None, right=None, parent=None):
            self.__value = value
            self.__left = left
            self.__right = right
            self.__parent = parent

        def __str__(self):
            """Binary Node to-string"""
            return f"|{self.__value}|"

        def __lt__(self, other):
            if type(self) == type(other):
                if type(other._BinaryNode__value) is int:
                    return self.__value < other._BinaryNode__value

                raise TypeError('Type of node value is not int')
            raise TypeError('Comparison node is not type BinaryNode')

        def __gt__(self, other):
            if type(self) == type(other):
                if type(other._BinaryNode__value) is int:
                    return self.__value > other._BinaryNode__value

                raise TypeError('Type of node value is not int')
            raise TypeError('Comparison node is not type BinaryNode')

        def __eq__(self, other):
            if type(self) == type(other):
                if type(other._BinaryNode__value) is int:
                    return self.__value == other._BinaryNode__value

                raise TypeError('Type of node value is not int')
            raise TypeError('Comparison node is not type BinaryNode')

    def __init__(self, root=None):
        self.__root = root
        self.__size = 0

    def __str__(self):
        """BST to-string"""
        return str(self.inorder_traversal())

    def __len__(self):
        """Number of nodes in tree"""
        return self.__size

    def inorder_traversal(self, node=None, result=None):
        """Recursive traversal to get every node"""
        """Inorder tree traversal"""
        if node is None:
            node = self.__root
        if result is None:
            result = []

        if node._BinaryNode__left is not None:
            self.inorder_traversal(node._BinaryNode__left, result)

        result.append(node._BinaryNode__value)

        if node._BinaryNode__right is not None:
            self.inorder_traversal(node._BinaryNode__right, result)

        return result

    def insert(self, value, currNode=None):
        """Add a value into the tree"""
        node = self.BinaryNode(value)

        if currNode is None:
            if self.__root is None:
                self.__root = node
                self.__size += 1
                return
            currNode = self.__root

        if node == currNode:
            raise Exception('Node is already present in tree')

        if type(value) is not int:
            raise TypeError('Value is not type int')

        if node < currNode:
            if currNode._BinaryNode__left is None:
                currNode._BinaryNode__left = node
                node._BinaryNode__parent = currNode
                self.__size += 1
                return
            else:
                self.insert(value, currNode=currNode._BinaryNode__left)
        elif node > currNode:
            if currNode._BinaryNode__right is None:
                currNode._BinaryNode__right = node
                node._BinaryNode__parent = currNode
                self.__size += 1
                return
            else:
                self.insert(value, currNode=currNode._BinaryNode__right)

    def get_min(self):
        """Get min node value in tree"""
        node = self.__root
        while node._BinaryNode__left is not None:
            node = node._BinaryNode__left
        return node

    def get_max(self):
        """Get max node value in tree"""
        node = self.__root
        while node._BinaryNode__right is not None:
            node = node._BinaryNode__right
        return node
