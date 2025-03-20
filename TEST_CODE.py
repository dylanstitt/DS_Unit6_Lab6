##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def VIEW_tree0():
    print("~" * 50)
    print(f"{P}This is what your tree looks like{W}\n")

    print("""
              (11)
            /     \\
          (1)      (16)
            \\     /  \\
            (7) (13)  (24)
                /     /
              (12)  (19)

    """)


def VIEW_tree1():
    print("~" * 50)
    print(f"{P}This is what your tree looks like{W}\n")

    print("""
              (11)
            /     \\
          (1)      (16)
            \\     /  \\
            (7) (13)  (24)
                      /
                    (19)

    """)


def VIEW_tree2():
    print("~" * 50)
    print(f"{P}This is what your tree looks like{W}\n")

    print("""
              (11)
             /    \\
           (7)     (16)
                   /  \\
                (13)  (19)


    """)
##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def TEST_parents(BST, curr=None, parent=None):
    if curr is None:
        curr = BST._BinarySearchTree__root

    # print(curr, "-", curr._BinaryNode__parent, parent)

    if curr._BinaryNode__parent is not parent:
        return 0

    L = R = 1

    if curr._BinaryNode__left is not None:
        L = TEST_parents(BST, curr._BinaryNode__left, curr)
    if curr._BinaryNode__right is not None:
        R = TEST_parents(BST, curr._BinaryNode__right, curr)

    return L * R


def initialize_BST(BST):
    vals = [11, 1, 16, 7, 24, 19, 13, 12]
    for v in vals:
        BST.insert(v)


def TEST_zero_child(BST):
    VIEW_tree0()

    # print("~" * 50)
    print(f"{P}TEST CATEGORY: Zero Child Deletion{W}\n")

    root = BST._BinarySearchTree__root

    print(f"{B}12 will be removed from the tree{W}\n")
    BST.delete(12)

    test = len(BST) == 7
    print(f"Tree size was reduced to 7: {result(test)}")

    test = root._BinaryNode__right._BinaryNode__left._BinaryNode__left is None
    print(f"Node 13 no longer has a left child: {result(test)}")

    test = BST.inorder_traversal() == [1, 7, 11, 13, 16, 19, 24]
    print(f"Node 12 is no longer in the tree: {result(test)}")

    test = TEST_parents(BST)
    print(f"\nParent/Child connections are correct: {result(bool(test))}")

    print(f"\n{B}99 will be removed from the tree{W}\n")
    try:
        BST.delete(99)
        print(f"Raise exception if value doesn't exist: {result(False)}")
    except:
        print(f"Raise exception if value doesn't exist: {result(True)}")

    test = TEST_parents(BST)
    print(f"\nParent/Child connections are correct: {result(bool(test))}")

    print("~" * 50, "\n\n")


def TEST_one_child(BST):
    VIEW_tree1()

    # print("~" * 50)
    print(f"{P}TEST CATEGORY: One Child Deletion{W}\n")

    root = BST._BinarySearchTree__root

    print(f"{B}1 will be removed from the tree{W}\n")
    BST.delete(1)

    test = len(BST) == 6
    print(f"Tree size was reduced to 6: {result(test)}")

    test = root._BinaryNode__left._BinaryNode__value == 7
    print(f"Node 11 has a new left child: {result(test)}")

    test = BST.inorder_traversal() == [7, 11, 13, 16, 19, 24]
    print(f"Node 1 is no longer in the tree: {result(test)}")

    test = TEST_parents(BST)
    print(f"\nParent/Child connections are correct: {result(bool(test))}")

    print(f"\n{B}24 will be removed from the tree{W}\n")
    BST.delete(24)

    test = len(BST) == 5
    print(f"Tree size was reduced to 5: {result(test)}")

    test = root._BinaryNode__right._BinaryNode__right._BinaryNode__value == 19
    print(f"Node 16 has a new right child: {result(test)}")

    test = BST.inorder_traversal() == [7, 11, 13, 16, 19]
    print(f"Node 24 is no longer in the tree: {result(test)}")

    test = TEST_parents(BST)
    print(f"\nParent/Child connections are correct: {result(bool(test))}")

    print("~" * 50, "\n\n")


def TEST_two_child(BST):
    VIEW_tree2()

    # print("~" * 50)
    print(f"{P}TEST CATEGORY: Two Child Deletion{W}\n")

    root = BST._BinarySearchTree__root

    print(f"{B}16 will be removed from the tree{W}\n")
    BST.delete(16)

    test = len(BST) == 4
    print(f"Tree size was reduced to 4: {result(test)}")

    test = root._BinaryNode__right._BinaryNode__value == 19
    print(f"Node 11 has a new right child: {result(test)}")

    test = BST.inorder_traversal() == [7, 11, 13, 19]
    print(f"Node 16 is no longer in the tree: {result(test)}")

    test = TEST_parents(BST)
    print(f"\nParent/Child connections are correct: {result(bool(test))}")

    print(f"\n{B}11 will be removed from the tree{W}\n")
    BST.delete(11)

    root = BST._BinarySearchTree__root

    test = len(BST) == 3
    print(f"Tree size was reduced to 3: {result(test)}")

    test = root._BinaryNode__value == 13
    print(f"Node 13 is the new root: {result(test)}")

    test = root._BinaryNode__left._BinaryNode__value == 7 and root._BinaryNode__right._BinaryNode__value == 19
    print(f"New root has correct children: {result(test)}")

    test = BST.inorder_traversal() == [7, 13, 19]
    print(f"Node 11 is no longer in the tree: {result(test)}")

    test = TEST_parents(BST)
    print(f"\nParent/Child connections are correct: {result(bool(test))}")

    print("~" * 50, "\n\n")


def TEST_docs(BST, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    doc = BST.insert.__doc__
    if doc != None:
        print(f"{B}insert() Documentation:{W} {doc}\n")
    else:
        print(f"{R}insert() Documentation Missing{W}\n")

    doc = BST.get_min.__doc__
    if doc != None:
        print(f"{B}get_min() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_min() Documentation Missing{W}\n")

    doc = BST.get_max.__doc__
    if doc != None:
        print(f"{B}get_max() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_max() Documentation Missing{W}\n")

    doc = BST.inorder_traversal.__doc__
    if doc != None:
        print(f"{B}inorder_traversal() Documentation:{W} {doc}\n")
    else:
        print(f"{R}inorder_traversal() Documentation Missing{W}\n")

    doc = BST.delete.__doc__
    if doc != None:
        print(f"{B}delete() Documentation:{W} {doc}\n")
    else:
        print(f"{R}delete() Documentation Missing{W}\n")

    doc = class_ref.__str__.__doc__
    if doc != None:
        print(f"{B}__str__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__str__() Documentation Missing{W}\n")

    doc = class_ref.__len__.__doc__
    if doc != None:
        print(f"{B}__len__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__len__() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")