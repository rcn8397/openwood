# -*- coding: utf-8 -*-
'''
BTree Primative

This work is based heavily on Introduction to Algorithms (third edition) and Wikipedia

Introduction to Algorithms
https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844
https://mitpress.mit.edu/books/introduction-algorithms-third-edition

Wikipedia:
https://en.wikipedia.org/wiki/Binary_search_tree#Operations

'''
from .visitor import *
from .bnode   import BNode

class Node( BNode ):
    '''
    Generic Tree Node
    '''
    def __init__( self, *args, **kwargs ):
        super( Node, self ).__init__( *args, **kwargs )

class Btree( object ):
    '''
    Binary Search Tree Graph
    '''
    def __init__( self, root = None ):
        super( Btree, self ).__init__()
        self.root = root
        self.nodes = list()
        self.graph = dict()

    def insert( self, key, value ):
        # If the trees root is None, set root to be tree root
        self.root = self.binary_insert( key, value, self.root )

    def binary_insert( self, key, value, node, parent = None ):
        if node is None:
            return Node( key, value, None, None, parent )
        elif key == node.key:
            return Node( key, value, node.left, node.right, node.parent )
        elif key < node.key:
            return Node( node.key,
                         node.value,
                         self.binary_insert( key, value, node.left, node ),
                         node.right,
                         node.parent )
        else:
            return Node( node.key,
                         node.value,
                         node.left,
                         self.binary_insert( key, value, node.right, node ),
                         node.parent )

    def bfs( self, node, visitor = DebugVisitor() ):
        '''
        Breadth-first search (connected components)

        node (Node) starting node
        '''
        from queue import Queue
        q = Queue()
        q.put( node )
        while not q.empty():
            v = q.get()

            # Accept visitor
            v.accept( visitor )

            if v.left is not None:
                q.put( v.left )
            if v.right is not None:
                q.put( v.right )

    def dfs( self, node, visitor = DebugVisitor(), order = None ):
        '''
        Depth first search
        '''
        if order is None:
            order = self.in_order
        order( node, visitor )

    def in_order( self, node, visitor ):
        '''
        In-order (LNR) tree traversal
        '''
        if node is None: return

        # Left node
        self.in_order( node.left, visitor )

        # Accept visitors
        node.accept( visitor )

        # Right node
        self.in_order( node.right, visitor )

    def pre_order( self, node, visitor ):
        '''
        Pre-order (NLR) tree traversal
        '''
        if node is None: return

        # Accept visitors
        node.accept( visitor )

        # Process nodes, left/right
        self.pre_order( node.left,  visitor )
        self.pre_order( node.right, visitor )

    def post_order( self, node, visitor ):
        '''
        Post-order (LRN) tree traversal
        '''
        if node is None: return

        # Process nodes, left/right
        self.post_order( node.left,  visitor )
        self.post_order( node.right, visitor )

        # Accept visitors
        node.accept( visitor )

    def as_dot( self, fname ):
        visitor = DotVisitor()
        self.bfs( self.root, visitor = visitor )
        visitor.write( fname )

    def search( self, key ):
        return self.binary_search( key, self.root )

    def binary_search( self, key, node ):
        '''
        Recursively search for key from node
        '''
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.binary_search( key, node.left )
        if key > node.key:
            return self.binary_search( key, node.right )

    @property
    def min( self ):
        return self.root.minimum()

    @property
    def max( self ):
        return self.root.maximum()

    def minimum( self, node ):
        return node.minimum()

    def maximum( self, node ):
        return node.maximum()

    def successor( self, node ):
        x = node
        if x.right is not None:
            return self.minimum( x.right )
        y = node.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def transplant( self, u, v ):
        '''
        Transplant subtree u, with subtree v
        '''
        if u.parent is None:
            # Handle case in which u is the root of the Tree
            self.root.replace_with( v )
        elif u == u.parent.left:
            # Update u's parent's left child
            u.parent.left.replace_with( v )
        else:
            # Update u's parent's left child
            u.parent.right.replace_with( v )
        if v is not None:
            # Update v's parent with u's parent
            v.parent.replace_with( u.parent )

    def delete_key( self, key ):
        node = self.search( key )
        self.delete( node )

    def delete( self, node ):
        if node.left is None:
            # If node has no left child, then replace this
            # node by its right child (which may be None)
            node.replace_with( node.right )
        elif node.left is not None and node.right is None:
            # If this node has just a left child, then
            # replace this node by its left child
            node.replace_with( node.left )
        else:
            # Else node has both left and right child nodes.

            # Find this nodes successor Y
            y = self.successor( node )

            if node.right == y:
                # If Y is this nodes right child, then replace it with Y
                node.replace_with( y )
            else:
                # Otherwise Y lies in this nodes right subtree but is
                # not this nodes right child

                # Replace Y by it's own right child
                y.replace_with( y.right )


                # Set Y to be the nodes right child parent.
                node.right.parent = y

                # Set Y's left child to be nodes left subtree
                y.left = node.left

                # Finally replace Y as node
                node.replace_with( y )
