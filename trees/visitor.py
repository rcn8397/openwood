# -*- coding: utf-8 -*-
'''
Vistor Patterns
'''

address_of = lambda x : hex( id( x ) )

class Visitor( object ):
    def __str__( self ):
        return self.__class__.__name__

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
