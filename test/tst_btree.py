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
        tree.insert( i, char )

    tree.dfs( tree.root )

    # Output draft as dot
    print( 'Writing tree to dot format' )
    tree.as_dot( 'test.dot' )

    # Search for the 4th
    fourth = tree.search( 4 )
    print( 'Searching for the node with the fourth key, found: [{0}]'.format( fourth.value ) )

    print( 'Tree minimum: {0}'.format( tree.min ) )
    print( 'Tree maximum: {0}'.format( tree.max ) )

    print( 'Searched Node\'s min: {0}, max: {1}'.format( fourth.minimum(),
                                                         fourth.maximum() ) )

    print( 'Attempting to delete the searched node' )
    tree.delete_key( fourth.key )

    # Output modified tree as dot
    print( 'Writing modified tree to dot format' )
    tree.as_dot( 'deleted.dot' )


# Standard biolerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()
