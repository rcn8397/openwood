#!/usr/bin/env python3
import sys, os
import pdb

# Setup root import paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from trees.btree import Btree

def test_btree():
    # Create an instance of the tree
    tree = Btree()
    assert tree

    # Fill the tree with data
    for i, char in enumerate( 'hello_world' ):
        tree.insert( i, char )

    # Search the tree
    # This should do something we can test in travis for
    tree.dfs( tree.root )

    # Output draft as dot
    print( 'Writing tree to dot format' )
    tree.as_dot( 'test.dot' )
    assert os.path.exists( 'test.dot' )

    # Search for the 4th
    print( 'Search for the node with key 4' )
    fourth = tree.search( 4 )
    assert fourth
    print( '{0} found with value: [{0}]'.format( fourth,
                                                 fourth.value ) )

    # Min/Max nodes
    tree_min = tree.min
    assert tree_min
    print( 'Tree minimum: {0}'.format( tree_min ) )
    
    tree_max = tree.max
    assert tree_max
    print( 'Tree maximum: {0}'.format( tree_max ) )

    fourth_min = fourth.minimum()
    assert fourth_min
    fourth_max = fourth.maximum()
    assert fourth_max
    print( 'Node\'s min: {0}, max: {1}'.format( fourth_min,
                                                fourth_max ) )

    # Deletion
    print( 'Attempting to delete the searched node' )
    tree.delete_key( fourth.key )
    fourth = tree.search( 4 )
    assert ( fourth is None )

    # Output modified tree as dot
    print( 'Writing modified tree to dot format' )
    tree.as_dot( 'deleted.dot' )
    assert os.path.exists( 'deleted.dot' )

    
# Main
def main():
    test_btree()

# Standard biolerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()
