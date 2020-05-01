# -*- coding: utf-8 -*-
'''
BTree Primative
'''
address_of = lambda x : hex( id( x ) )

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

    def label( self ):
        return '{0}({1})'.format( self.value, self.key )

    def address( self ):
        return hex( id( self ) )
    def __str__( self ):
        return str( self.value )

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

class DotVisitor( Visitor ):
    def __init__( self ):
        super( DotVisitor, self ).__init__()
        self.dot_header = 'graph G {\n'
        self.dot_labels = ''
        self.dot_ranks  = ''
        self.dot_nodes  = ''
        self.dot_footer = '}\n'

        # Create a Null (None) node label
        self.dot_labels += self.add_label( address_of(None), 'None')

    def write( self, fname ):
        with open( fname, 'w' ) as f:
            f.write( self.dot_header )
            f.write( self.dot_labels )
            f.write( self.dot_ranks  )
            f.write( self.dot_nodes  )
            f.write( self.dot_footer )

    def add_label( self, node, label ):
        return '"{0}" [label="{1}"];\n'.format(node,label)

    def append_label( self, node ):
        self.dot_labels += self.add_label( address_of(node),
                                           node.label() )

    def append_node( self, node ):
        add_edge = lambda u, v : '"{0}" -- "{1}"\n'.format( u, v )
        self.dot_nodes += add_edge( address_of(node),
                                    address_of(node.left ) )
        self.dot_nodes += add_edge( address_of(node),
                                    address_of(node.right) )

    def visit( self, node ):
        self.append_label( node )
        self.append_node( node )

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
        pass

    def delete( self, key ):
        pass

    def traverse( self, node, proc ):
        pass
