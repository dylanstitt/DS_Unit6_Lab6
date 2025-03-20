# Dylan Stitt
# Unit 6 Lab 6
# Binary Search Tree Delete

# Implementation & testing of the Binary Search Tree

# Import file
from TEST_CODE import *
import os
from BinarySearchTree import BinarySearchTree

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():

    BST = BinarySearchTree()

    # Add nodes to test tree
    initialize_BST(BST)

    # TEST 1 - Test Zero-Child deletion
    # BEFORE TESTING: implement delete
    TEST_zero_child(BST)

    # TEST 2 - Test One-Child deletion
    # BEFORE TESTING: implement delete
    TEST_one_child(BST)

    # TEST 3 - Test Two-Child deletion
    # BEFORE TESTING: implement delete
    TEST_two_child(BST)

    # TEST 4 - Test docstrings
    # BEFORE TESTING: implement docstrings
    #TEST_docs(BST, BinarySearchTree)

if __name__ == "__main__":
    os.system("cls")
    main()
