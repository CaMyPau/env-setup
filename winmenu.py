#!/usr/bin/env python3
# dmenu script to jump to windows in i3.
#
# Based on original script by Jure Ziberna
#
# using ziberna's i3-py library: https://github.com/ziberna/i3-py
# depends: dmenu (vertical patch), i3.
# released by joepd under WTFPLv2-license:
# http://sam.zoy.org/wtfpl/COPYING
#
# edited by Jure Ziberna for i3-py's examples section

import sys
import subprocess
import i3

def workspaces():
    reply = i3.msg( 'get_workspaces' )
    return [ w[ 'name' ] for w in reply ]

def win_menu( clients ):
    """
    Displays a window menu using dmenu. Returns window id.
    """

    command = [ '/usr/bin/dmenu' ]
    command += sys.argv[ 1 : ]

    dmenu = subprocess.Popen( command
                            , stdin  = subprocess.PIPE
                            , stdout = subprocess.PIPE )

    menu_str = '\n'.join( sorted( clients ) )
    # Popen.communicate returns a tuple stdout, stderr
    win_str = dmenu.communicate( menu_str.encode( 'utf-8' ) )[ 0 ].decode( 'utf-8' ).rstrip()
    return win_str

if __name__ == '__main__':
    clients = workspaces()
    ws_name = win_menu( clients )
    if ws_name:
        i3.msg( 'command', 'workspace ' + ws_name )
