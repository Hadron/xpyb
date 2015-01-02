#
# This file generated automatically from render.xml by py_client.py.
# Edit at your peril.
#

import xcb
import cStringIO
from struct import pack, unpack_from
from array import array
import xproto

MAJOR_VERSION = 0
MINOR_VERSION = 11

key = xcb.ExtensionKey('RENDER')

class PictType:
    Indexed = 0
    Direct = 1

class Picture:
    _None = 0

class PictOp:
    Clear = 0
    Src = 1
    Dst = 2
    Over = 3
    OverReverse = 4
    In = 5
    InReverse = 6
    Out = 7
    OutReverse = 8
    Atop = 9
    AtopReverse = 10
    Xor = 11
    Add = 12
    Saturate = 13
    DisjointClear = 16
    DisjointSrc = 17
    DisjointDst = 18
    DisjointOver = 19
    DisjointOverReverse = 20
    DisjointIn = 21
    DisjointInReverse = 22
    DisjointOut = 23
    DisjointOutReverse = 24
    DisjointAtop = 25
    DisjointAtopReverse = 26
    DisjointXor = 27
    ConjointClear = 32
    ConjointSrc = 33
    ConjointDst = 34
    ConjointOver = 35
    ConjointOverReverse = 36
    ConjointIn = 37
    ConjointInReverse = 38
    ConjointOut = 39
    ConjointOutReverse = 40
    ConjointAtop = 41
    ConjointAtopReverse = 42
    ConjointXor = 43
    Multiply = 48
    Screen = 49
    Overlay = 50
    Darken = 51
    Lighten = 52
    ColorDodge = 53
    ColorBurn = 54
    HardLight = 55
    SoftLight = 56
    Difference = 57
    Exclusion = 58
    HSLHue = 59
    HSLSaturation = 60
    HSLColor = 61
    HSLLuminosity = 62

class PolyEdge:
    Sharp = 0
    Smooth = 1

class PolyMode:
    Precise = 0
    Imprecise = 1

class CP:
    Repeat = 1
    AlphaMap = 2
    AlphaXOrigin = 4
    AlphaYOrigin = 8
    ClipXOrigin = 16
    ClipYOrigin = 32
    ClipMask = 64
    GraphicsExposure = 128
    SubwindowMode = 256
    PolyEdge = 512
    PolyMode = 1024
    Dither = 2048
    ComponentAlpha = 4096

class SubPixel:
    Unknown = 0
    HorizontalRGB = 1
    HorizontalBGR = 2
    VerticalRGB = 3
    VerticalBGR = 4
    _None = 5

class Repeat:
    _None = 0
    Normal = 1
    Pad = 2
    Reflect = 3

class PictFormatError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadPictFormat(xcb.ProtocolException):
    pass

class PictureError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadPicture(xcb.ProtocolException):
    pass

class PictOpError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadPictOp(xcb.ProtocolException):
    pass

class GlyphSetError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadGlyphSet(xcb.ProtocolException):
    pass

class GlyphError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadGlyph(xcb.ProtocolException):
    pass

class DIRECTFORMAT(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.red_shift, self.red_mask, self.green_shift, self.green_mask, self.blue_shift, self.blue_mask, self.alpha_shift, self.alpha_mask,) = unpack_from('HHHHHHHH', parent, offset)

class PICTFORMINFO(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.id, self.type, self.depth,) = unpack_from('IBB2x', parent, offset)
        offset += 8
        self.direct = DIRECTFORMAT(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        (self.colormap,) = unpack_from('I', parent, offset)

class PICTVISUAL(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.visual, self.format,) = unpack_from('II', parent, offset)

class PICTDEPTH(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.depth, self.num_visuals,) = unpack_from('BxH4x', parent, offset)
        offset += 8
        self.visuals = xcb.List(parent, offset, self.num_visuals, PICTVISUAL, 8)
        offset += len(self.visuals.buf())
        xcb._resize_obj(self, offset - base)

class PICTSCREEN(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.num_depths, self.fallback,) = unpack_from('II', parent, offset)
        offset += 8
        self.depths = xcb.List(parent, offset, self.num_depths, PICTDEPTH, -1)
        offset += len(self.depths.buf())
        xcb._resize_obj(self, offset - base)

class INDEXVALUE(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.pixel, self.red, self.green, self.blue, self.alpha,) = unpack_from('IHHHH', parent, offset)

class COLOR(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.red, self.green, self.blue, self.alpha,) = unpack_from('HHHH', parent, offset)

class POINTFIX(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.x, self.y,) = unpack_from('ii', parent, offset)

class LINEFIX(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        self.p1 = POINTFIX(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.p2 = POINTFIX(parent, offset, 8)

class TRIANGLE(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        self.p1 = POINTFIX(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.p2 = POINTFIX(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.p3 = POINTFIX(parent, offset, 8)

class TRAPEZOID(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.top, self.bottom,) = unpack_from('ii', parent, offset)
        offset += 8
        self.left = LINEFIX(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(16, offset)
        self.right = LINEFIX(parent, offset, 16)

class GLYPHINFO(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.width, self.height, self.x, self.y, self.x_off, self.y_off,) = unpack_from('HHhhhh', parent, offset)

class QueryVersionCookie(xcb.Cookie):
    pass

class QueryVersionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.major_version, self.minor_version,) = unpack_from('xx2x4xII16x', parent, offset)

class QueryPictFormatsCookie(xcb.Cookie):
    pass

class QueryPictFormatsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_formats, self.num_screens, self.num_depths, self.num_visuals, self.num_subpixel,) = unpack_from('xx2x4xIIIII4x', parent, offset)
        offset += 32
        self.formats = xcb.List(parent, offset, self.num_formats, PICTFORMINFO, 28)
        offset += len(self.formats.buf())
        offset += xcb.type_pad(4, offset)
        self.screens = xcb.List(parent, offset, self.num_screens, PICTSCREEN, -1)
        offset += len(self.screens.buf())
        offset += xcb.type_pad(4, offset)
        self.subpixels = xcb.List(parent, offset, self.num_subpixel, 'I', 4)

class QueryPictIndexValuesCookie(xcb.Cookie):
    pass

class QueryPictIndexValuesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_values,) = unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.values = xcb.List(parent, offset, self.num_values, INDEXVALUE, 12)

class TRANSFORM(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.matrix11, self.matrix12, self.matrix13, self.matrix21, self.matrix22, self.matrix23, self.matrix31, self.matrix32, self.matrix33,) = unpack_from('iiiiiiiii', parent, offset)

class QueryFiltersCookie(xcb.Cookie):
    pass

class QueryFiltersReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_aliases, self.num_filters,) = unpack_from('xx2x4xII16x', parent, offset)
        offset += 32
        self.aliases = xcb.List(parent, offset, self.num_aliases, 'H', 2)
        offset += len(self.aliases.buf())
        offset += xcb.type_pad(4, offset)
        self.filters = xcb.List(parent, offset, self.num_filters, STR, -1)

class ANIMCURSORELT(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.cursor, self.delay,) = unpack_from('II', parent, offset)

class SPANFIX(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.l, self.r, self.y,) = unpack_from('iii', parent, offset)

class TRAP(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        self.top = SPANFIX(parent, offset, 12)
        offset += 12
        offset += xcb.type_pad(12, offset)
        self.bot = SPANFIX(parent, offset, 12)

class renderExtension(xcb.Extension):

    def QueryVersion(self, client_major_version, client_minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', client_major_version, client_minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, True),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def QueryVersionUnchecked(self, client_major_version, client_minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', client_major_version, client_minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, False),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def QueryPictFormats(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, True),
                                 QueryPictFormatsCookie(),
                                 QueryPictFormatsReply)

    def QueryPictFormatsUnchecked(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, False),
                                 QueryPictFormatsCookie(),
                                 QueryPictFormatsReply)

    def QueryPictIndexValues(self, format):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', format))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, True),
                                 QueryPictIndexValuesCookie(),
                                 QueryPictIndexValuesReply)

    def QueryPictIndexValuesUnchecked(self, format):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', format))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, False),
                                 QueryPictIndexValuesCookie(),
                                 QueryPictIndexValuesReply)

    def CreatePictureChecked(self, pid, drawable, format, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIII', pid, drawable, format, value_mask))
        buf.write(str(buffer(array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, True),
                                 xcb.VoidCookie())

    def CreatePicture(self, pid, drawable, format, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIII', pid, drawable, format, value_mask))
        buf.write(str(buffer(array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, False),
                                 xcb.VoidCookie())

    def ChangePictureChecked(self, picture, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', picture, value_mask))
        buf.write(str(buffer(array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, True),
                                 xcb.VoidCookie())

    def ChangePicture(self, picture, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', picture, value_mask))
        buf.write(str(buffer(array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, False),
                                 xcb.VoidCookie())

    def SetPictureClipRectanglesChecked(self, picture, clip_x_origin, clip_y_origin, rectangles_len, rectangles):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhh', picture, clip_x_origin, clip_y_origin))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, True),
                                 xcb.VoidCookie())

    def SetPictureClipRectangles(self, picture, clip_x_origin, clip_y_origin, rectangles_len, rectangles):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhh', picture, clip_x_origin, clip_y_origin))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, False),
                                 xcb.VoidCookie())

    def FreePictureChecked(self, picture):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, True),
                                 xcb.VoidCookie())

    def FreePicture(self, picture):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, False),
                                 xcb.VoidCookie())

    def CompositeChecked(self, op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhhhhhhHH', op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, True),
                                 xcb.VoidCookie())

    def Composite(self, op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhhhhhhHH', op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, False),
                                 xcb.VoidCookie())

    def TrapezoidsChecked(self, op, src, dst, mask_format, src_x, src_y, traps_len, traps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(traps, 10, 'traps', True):
            buf.write(pack('=iiiiiiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 10, True, True),
                                 xcb.VoidCookie())

    def Trapezoids(self, op, src, dst, mask_format, src_x, src_y, traps_len, traps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(traps, 10, 'traps', True):
            buf.write(pack('=iiiiiiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 10, True, False),
                                 xcb.VoidCookie())

    def TrianglesChecked(self, op, src, dst, mask_format, src_x, src_y, triangles_len, triangles):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(triangles, 6, 'triangles', True):
            buf.write(pack('=iiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, True),
                                 xcb.VoidCookie())

    def Triangles(self, op, src, dst, mask_format, src_x, src_y, triangles_len, triangles):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(triangles, 6, 'triangles', True):
            buf.write(pack('=iiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, False),
                                 xcb.VoidCookie())

    def TriStripChecked(self, op, src, dst, mask_format, src_x, src_y, points_len, points):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(pack('=ii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, True),
                                 xcb.VoidCookie())

    def TriStrip(self, op, src, dst, mask_format, src_x, src_y, points_len, points):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(pack('=ii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, False),
                                 xcb.VoidCookie())

    def TriFanChecked(self, op, src, dst, mask_format, src_x, src_y, points_len, points):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(pack('=ii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, True),
                                 xcb.VoidCookie())

    def TriFan(self, op, src, dst, mask_format, src_x, src_y, points_len, points):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(pack('=ii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, False),
                                 xcb.VoidCookie())

    def CreateGlyphSetChecked(self, gsid, format):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', gsid, format))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, True),
                                 xcb.VoidCookie())

    def CreateGlyphSet(self, gsid, format):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', gsid, format))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, False),
                                 xcb.VoidCookie())

    def ReferenceGlyphSetChecked(self, gsid, existing):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', gsid, existing))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, True),
                                 xcb.VoidCookie())

    def ReferenceGlyphSet(self, gsid, existing):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', gsid, existing))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, False),
                                 xcb.VoidCookie())

    def FreeGlyphSetChecked(self, glyphset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', glyphset))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, True),
                                 xcb.VoidCookie())

    def FreeGlyphSet(self, glyphset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', glyphset))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, False),
                                 xcb.VoidCookie())

    def AddGlyphsChecked(self, glyphset, glyphs_len, glyphids, glyphs, data_len, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', glyphset, glyphs_len))
        buf.write(str(buffer(array('I', glyphids))))
        for elt in xcb.Iterator(glyphs, 6, 'glyphs', True):
            buf.write(pack('=HHhhhh', *elt))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 20, True, True),
                                 xcb.VoidCookie())

    def AddGlyphs(self, glyphset, glyphs_len, glyphids, glyphs, data_len, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', glyphset, glyphs_len))
        buf.write(str(buffer(array('I', glyphids))))
        for elt in xcb.Iterator(glyphs, 6, 'glyphs', True):
            buf.write(pack('=HHhhhh', *elt))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 20, True, False),
                                 xcb.VoidCookie())

    def FreeGlyphsChecked(self, glyphset, glyphs_len, glyphs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', glyphset))
        buf.write(str(buffer(array('I', glyphs))))
        return self.send_request(xcb.Request(buf.getvalue(), 22, True, True),
                                 xcb.VoidCookie())

    def FreeGlyphs(self, glyphset, glyphs_len, glyphs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', glyphset))
        buf.write(str(buffer(array('I', glyphs))))
        return self.send_request(xcb.Request(buf.getvalue(), 22, True, False),
                                 xcb.VoidCookie())

    def CompositeGlyphs8Checked(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 23, True, True),
                                 xcb.VoidCookie())

    def CompositeGlyphs8(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 23, True, False),
                                 xcb.VoidCookie())

    def CompositeGlyphs16Checked(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 24, True, True),
                                 xcb.VoidCookie())

    def CompositeGlyphs16(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 24, True, False),
                                 xcb.VoidCookie())

    def CompositeGlyphs32Checked(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 25, True, True),
                                 xcb.VoidCookie())

    def CompositeGlyphs32(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 25, True, False),
                                 xcb.VoidCookie())

    def FillRectanglesChecked(self, op, dst, color, rects_len, rects):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xI', op, dst))
        for elt in xcb.Iterator(color, 4, 'color', False):
            buf.write(pack('=HHHH', *elt))
        for elt in xcb.Iterator(rects, 4, 'rects', True):
            buf.write(pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 26, True, True),
                                 xcb.VoidCookie())

    def FillRectangles(self, op, dst, color, rects_len, rects):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xI', op, dst))
        for elt in xcb.Iterator(color, 4, 'color', False):
            buf.write(pack('=HHHH', *elt))
        for elt in xcb.Iterator(rects, 4, 'rects', True):
            buf.write(pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 26, True, False),
                                 xcb.VoidCookie())

    def CreateCursorChecked(self, cid, source, x, y):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHH', cid, source, x, y))
        return self.send_request(xcb.Request(buf.getvalue(), 27, True, True),
                                 xcb.VoidCookie())

    def CreateCursor(self, cid, source, x, y):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHH', cid, source, x, y))
        return self.send_request(xcb.Request(buf.getvalue(), 27, True, False),
                                 xcb.VoidCookie())

    def SetPictureTransformChecked(self, picture, transform):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(transform, 9, 'transform', False):
            buf.write(pack('=iiiiiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 28, True, True),
                                 xcb.VoidCookie())

    def SetPictureTransform(self, picture, transform):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(transform, 9, 'transform', False):
            buf.write(pack('=iiiiiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 28, True, False),
                                 xcb.VoidCookie())

    def QueryFilters(self, drawable):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', drawable))
        return self.send_request(xcb.Request(buf.getvalue(), 29, False, True),
                                 QueryFiltersCookie(),
                                 QueryFiltersReply)

    def QueryFiltersUnchecked(self, drawable):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', drawable))
        return self.send_request(xcb.Request(buf.getvalue(), 29, False, False),
                                 QueryFiltersCookie(),
                                 QueryFiltersReply)

    def SetPictureFilterChecked(self, picture, filter_len, filter, values_len, values):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', picture, filter_len))
        buf.write(str(buffer(array('b', filter))))
        buf.write(str(buffer(array('i', values))))
        return self.send_request(xcb.Request(buf.getvalue(), 30, True, True),
                                 xcb.VoidCookie())

    def SetPictureFilter(self, picture, filter_len, filter, values_len, values):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', picture, filter_len))
        buf.write(str(buffer(array('b', filter))))
        buf.write(str(buffer(array('i', values))))
        return self.send_request(xcb.Request(buf.getvalue(), 30, True, False),
                                 xcb.VoidCookie())

    def CreateAnimCursorChecked(self, cid, cursors_len, cursors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', cid))
        for elt in xcb.Iterator(cursors, 2, 'cursors', True):
            buf.write(pack('=II', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 31, True, True),
                                 xcb.VoidCookie())

    def CreateAnimCursor(self, cid, cursors_len, cursors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', cid))
        for elt in xcb.Iterator(cursors, 2, 'cursors', True):
            buf.write(pack('=II', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 31, True, False),
                                 xcb.VoidCookie())

    def AddTrapsChecked(self, picture, x_off, y_off, traps_len, traps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhh', picture, x_off, y_off))
        for elt in xcb.Iterator(traps, 6, 'traps', True):
            buf.write(pack('=iiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 32, True, True),
                                 xcb.VoidCookie())

    def AddTraps(self, picture, x_off, y_off, traps_len, traps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhh', picture, x_off, y_off))
        for elt in xcb.Iterator(traps, 6, 'traps', True):
            buf.write(pack('=iiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 32, True, False),
                                 xcb.VoidCookie())

    def CreateSolidFillChecked(self, picture, color):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(color, 4, 'color', False):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 33, True, True),
                                 xcb.VoidCookie())

    def CreateSolidFill(self, picture, color):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(color, 4, 'color', False):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 33, True, False),
                                 xcb.VoidCookie())

    def CreateLinearGradientChecked(self, picture, p1, p2, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(p1, 2, 'p1', False):
            buf.write(pack('=ii', *elt))
        for elt in xcb.Iterator(p2, 2, 'p2', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=I', num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 34, True, True),
                                 xcb.VoidCookie())

    def CreateLinearGradient(self, picture, p1, p2, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(p1, 2, 'p1', False):
            buf.write(pack('=ii', *elt))
        for elt in xcb.Iterator(p2, 2, 'p2', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=I', num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 34, True, False),
                                 xcb.VoidCookie())

    def CreateRadialGradientChecked(self, picture, inner, outer, inner_radius, outer_radius, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(inner, 2, 'inner', False):
            buf.write(pack('=ii', *elt))
        for elt in xcb.Iterator(outer, 2, 'outer', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=iiI', inner_radius, outer_radius, num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 35, True, True),
                                 xcb.VoidCookie())

    def CreateRadialGradient(self, picture, inner, outer, inner_radius, outer_radius, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(inner, 2, 'inner', False):
            buf.write(pack('=ii', *elt))
        for elt in xcb.Iterator(outer, 2, 'outer', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=iiI', inner_radius, outer_radius, num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 35, True, False),
                                 xcb.VoidCookie())

    def CreateConicalGradientChecked(self, picture, center, angle, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(center, 2, 'center', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=iI', angle, num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 36, True, True),
                                 xcb.VoidCookie())

    def CreateConicalGradient(self, picture, center, angle, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(center, 2, 'center', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=iI', angle, num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 36, True, False),
                                 xcb.VoidCookie())

_events = {
}

_errors = {
    0 : (PictFormatError, BadPictFormat),
    1 : (PictureError, BadPicture),
    2 : (PictOpError, BadPictOp),
    3 : (GlyphSetError, BadGlyphSet),
    4 : (GlyphError, BadGlyph),
}

xcb._add_ext(key, renderExtension, _events, _errors)
