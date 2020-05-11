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

address_of = lambda x : hex( id( x ) )

class Visitor( object ):
    def __str__( self ):
        return self.__class__.__name__

class Node( object ):
    '''
    Generic Tree Node
    '''
    def __init__( self, key = None, value = None, left = None, right = None, parent = None ):
        self.value  = value
        self.key    = key
        self.left   = left
        self.right  = right
        self.parent = parent

    def replace_with( self, node ):
        self.value  = node.value
        self.key    = node.key
        self.left   = node.left
        self.right  = node.right
        self.parent = node.parent

    def label( self ):
        return '{0}({1})'.format( self.value, self.key )

    def address( self ):
        return hex( id( self ) )
    def __str__( self ):
        return str( self.value )

    def debug( self ):
        print( '\n/// {0} ///'.format( str( self ) ) )
        for member in vars( self ):
            print( '{0:10} = {1}'.format( member, vars( self )[ member ] ) )

    def maximum( self ):
        '''Find maximum node in this nodes subtree'''
        current = self
        while current.right:
            current = current.right
        return current

    def minimum( self ):
        '''Find minimum node in this nodes subtree'''
        current = self
        while current.left:
            current = current.left
        return current

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
