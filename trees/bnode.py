# -*- coding: utf-8 -*-
'''
Binary Node Primative

This work is based heavily on Introduction to Algorithms (third edition) and Wikipedia

Introduction to Algorithms
https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844
https://mitpress.mit.edu/books/introduction-algorithms-third-edition

Wikipedia:
https://en.wikipedia.org/wiki/Binary_search_tree#Operations

'''

class BNode( object ):
    '''
    Generic Binary Tree Node
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
