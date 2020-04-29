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
        self.value  = value
        self.key    = key       
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
        
class Btree( object ):
    '''
    Binary Search Tree Graph
    '''
    def __init__( self, root = None ):
        super( Tree, self ).__init__()
        self.root = root
        self.nodes = list()
        self.graph = dict()

    def insert( self, key, value, root = self.root, template = Node ):
        # Create a new node with key, value parameters
        node = template( key, value )

        # If there is no root, set the node as the root
        if root is None:
            root = node            
        # If the key matches the root's key, set the roots value 
        elif key == root.key:
            root.value = value
        # If the key is less than this roots key insert it on the left
        elif key < root.key:
            self.insert_at( key, value, root.left, template )
        # Finally, if the key is greater, insert it on the right
        else:
            self.insert_at( key, value, root.right, template )        

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
