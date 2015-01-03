import sys

if sys.version_info[0] < 3:
    from xcb import *
else:
    from xcb.xcb import *

__all__ = [ 'xproto', 'bigreq', 'xc_misc' ]
