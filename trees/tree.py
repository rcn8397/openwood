# -*- coding: utf-8 -*-
'''
Tree Primative
'''
class Visitor( object ):
    def __str__( self ):
        return self.__class__.__name__

class Node( object ):
    '''
    Generic Tree Node
    '''
    def __init__( self, key = None, value = None ):
        self._value = value
        self._key   = key       
        self.left   = None
        self.right  = None
        self.parent = None

    def accept( self, visitor ):
        '''
        Accept a visitor
        '''
        visitor.visit( self )

class DebugVisitor( Visitor ):
    def visit( self, node ):
        print( node )
        
class Tree( object ):
    '''
    Tree Graph
    '''
    def __init__( self, root = None ):
        super( Tree, self ).__init__()
        self.root = root
        self.nodes = list()
        self.graph = dict()
        
    def add_edge( self, u, v ):
        '''
        Add an edge to the tree
        '''
        self.graph[ u ].append( v )
        
    def insert( self, node, parent = None ):
        self.nodes.append( node )
        if parent is not None:
            parent.append( node )
            self.add_edge( parent, node )

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
        
    def dfs( self, node, visitor = DebugVisitor(), order = self.in_order ):
        '''
        Depth first search
        '''
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
