#!/usr/bin/env python3
import sys, os
import pdb

# Setup root import paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from trees.btree import Btree


# Main
def main():
    tree = Btree()
    
    for i, char in enumerate( 'hello_world' ):
        tree.insert( ord(char), char )

    tree.dfs( tree.root )
    
    
# Standard biolerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()
