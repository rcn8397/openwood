#!/usr/bin/env python3
import sys, os
import fnmatch
from subprocess import Popen, PIPE
import shlex

def find( path, patterns ):
     '''
     Find all files with ext patterns
     '''
     is_ext = lambda f, ext : any( f.endswith( e ) for e in ext )
     matches = []
     for root, dirs, files in os.walk( path, topdown=True ):
         for filename in files:
             if is_ext( filename.lower(), patterns ):
                 match = os.path.join( root, filename )
                 matches.append( match )
     return matches

class Subprocess( object ):
    '''
    Subprocess object
    '''
    def __init__( self, cmd = [ 'echo', 'hello world' ] ):
        super( Subprocess, self ).__init__()
        self._cmd = cmd
        self._stdout = []
        self._proc = Popen( cmd, stdout=PIPE, bufsize=1 )
        with self._proc.stdout:
            for line in iter( self._proc.stdout.readline, b'' ):
                self._stdout.append( line )
        self._proc.wait()

    def output( self ):
        for line in self._stdout:
            yield line

    def dump( self ):
        for line in self._stdout:
            print( line )
            
# Main
def main():
    dot_files = find( '.', ['.dot'] )

    for dot in dot_files:
        print( 'Converting {0} to png'.format( dot ) )
        cmd = 'dot -Tpng -O "{0}"'
        proc = Subprocess( shlex.split( cmd.format( dot ) ) )
        
        

# Standard biolerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()
