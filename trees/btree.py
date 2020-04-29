# -*- coding: utf-8 -*-
'''
BTree Primative
'''
class Visitor( object ):
    def __str__( self ):
        return self.__class__.__name__

class Node( object ):
    '''
    Generic Tree Node
    '''
    def __init__( self, key = None, value = None, left = None, right = None ):
        self.value  = value
        self.key    = key
        self.left   = left
        self.right  = right

    def debug( self ):
        for member in vars( self ):
            print( '{0:10} = {1}'.format( member, vars( self )[ member ] ) )

    def accept( self, visitor ):
        '''
        Accept a visitor
        '''
        visitor.visit( self )

class DebugVisitor( Visitor ):
    def visit( self, node ):
        node.debug()

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

    def binary_insert( self, key, value, node ):
        if node is None:
            return Node( key, value )
        elif key == node.key:
            return Node( key, value, node.left, node.right )
        elif key < node.key:
            return Node( node.key,
                         node.value,
                         self.binary_insert( key, value, node.left ),
                         node.right )
        else:
            return Node( node.key,
                         node.value,
                         node.left,
                         self.binary_insert( key, value, node.right ) )

    def bfs( self, node, visitor = DebugVisitor() ):
        '''
        Breadth-first search (connected components)

        node (Node) starting node
        '''
        from queue import Queue
        q = Queue()
        q.enque( node )
        while not q.empty():
            v = q.get()

            # Accept visitor
            v.accept( vistor )

            if v.left is not None:
                q.enqueu( v.left )
            if v.right is not None:
                q.enqueu( v.right )

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


    def search( self, key ):
        pass

    def delete( self, key ):
        pass

    def traverse( self, node, proc ):
        pass
