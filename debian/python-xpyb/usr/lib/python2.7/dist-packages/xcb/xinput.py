#
# This file generated automatically from xinput.xml by py_client.py.
# Edit at your peril.
#

import xcb
import cStringIO
from struct import pack, unpack_from
from array import array
import xproto
import render
import shape
import xfixes

MAJOR_VERSION = 2
MINOR_VERSION = 3

key = xcb.ExtensionKey('XInputExtension')

class FP3232(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.integral, self.frac,) = unpack_from('iI', parent, offset)

class GetExtensionVersionCookie(xcb.Cookie):
    pass

class GetExtensionVersionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.server_major, self.server_minor, self.present,) = unpack_from('xx2x4xHHB19x', parent, offset)

class DeviceUse:
    IsXPointer = 0
    IsXKeyboard = 1
    IsXExtensionDevice = 2
    IsXExtensionKeyboard = 3
    IsXExtensionPointer = 4

class InputClass:
    Key = 0
    Button = 1
    Valuator = 2
    Feedback = 3
    Proximity = 4
    Focus = 5
    Other = 6

class ValuatorMode:
    Relative = 0
    Absolute = 1

class DeviceInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.device_type, self.device_id, self.num_class_info, self.device_use,) = unpack_from('IBBBx', parent, offset)

class KeyInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.len, self.min_keycode, self.max_keycode, self.num_keys,) = unpack_from('BBBBH2x', parent, offset)

class ButtonInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.len, self.num_buttons,) = unpack_from('BBH', parent, offset)

class AxisInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.resolution, self.minimum, self.maximum,) = unpack_from('Iii', parent, offset)

class ValuatorInfo(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.class_id, self.len, self.axes_len, self.mode, self.motion_size,) = unpack_from('BBBBI', parent, offset)
        offset += 8
        self.axes = xcb.List(parent, offset, self.axes_len, AxisInfo, 12)
        offset += len(self.axes.buf())
        xcb._resize_obj(self, offset - base)

class InputInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.len,) = unpack_from('BB', parent, offset)

class DeviceName(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.len,) = unpack_from('B', parent, offset)
        offset += 1
        self.string = xcb.List(parent, offset, self.len, 'b', 1)
        offset += len(self.string.buf())
        xcb._resize_obj(self, offset - base)

class ListInputDevicesCookie(xcb.Cookie):
    pass

class ListInputDevicesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.devices_len,) = unpack_from('xx2x4xB23x', parent, offset)
        offset += 32
        self.devices = xcb.List(parent, offset, self.devices_len, DeviceInfo, 8)

class InputClassInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.event_type_base,) = unpack_from('BB', parent, offset)

class OpenDeviceCookie(xcb.Cookie):
    pass

class OpenDeviceReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_classes,) = unpack_from('xx2x4xB23x', parent, offset)
        offset += 32
        self.class_info = xcb.List(parent, offset, self.num_classes, InputClassInfo, 2)

class SetDeviceModeCookie(xcb.Cookie):
    pass

class SetDeviceModeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class GetSelectedExtensionEventsCookie(xcb.Cookie):
    pass

class GetSelectedExtensionEventsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_this_classes, self.num_all_classes,) = unpack_from('xx2x4xHH20x', parent, offset)
        offset += 32
        self.this_classes = xcb.List(parent, offset, self.num_this_classes, 'I', 4)
        offset += len(self.this_classes.buf())
        offset += xcb.type_pad(4, offset)
        self.all_classes = xcb.List(parent, offset, self.num_all_classes, 'I', 4)

class PropagateMode:
    AddToList = 0
    DeleteFromList = 1

class GetDeviceDontPropagateListCookie(xcb.Cookie):
    pass

class GetDeviceDontPropagateListReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_classes,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.classes = xcb.List(parent, offset, self.num_classes, 'I', 4)

class DeviceTimeCoord(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.time,) = unpack_from('I', parent, offset)

class GetDeviceMotionEventsCookie(xcb.Cookie):
    pass

class GetDeviceMotionEventsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_events, self.num_axes, self.device_mode,) = unpack_from('xx2x4xIBB18x', parent, offset)

class ChangeKeyboardDeviceCookie(xcb.Cookie):
    pass

class ChangeKeyboardDeviceReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class ChangePointerDeviceCookie(xcb.Cookie):
    pass

class ChangePointerDeviceReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class GrabDeviceCookie(xcb.Cookie):
    pass

class GrabDeviceReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class DeviceInputMode:
    AsyncThisDevice = 0
    SyncThisDevice = 1
    ReplayThisDevice = 2
    AsyncOtherDevices = 3
    AsyncAll = 4
    SyncAll = 5

class GetDeviceFocusCookie(xcb.Cookie):
    pass

class GetDeviceFocusReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.focus, self.time, self.revert_to,) = unpack_from('xx2x4xIIB15x', parent, offset)

class FeedbackClass:
    Keyboard = 0
    Pointer = 1
    String = 2
    Integer = 3
    Led = 4
    Bell = 5

class KbdFeedbackState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.pitch, self.duration, self.led_mask, self.led_values, self.global_auto_repeat, self.click, self.percent,) = unpack_from('BBHHHIIBBBx', parent, offset)
        offset += 20
        self.auto_repeats = xcb.List(parent, offset, 32, 'B', 1)

class PtrFeedbackState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.accel_num, self.accel_denom, self.threshold,) = unpack_from('BBH2xHHH', parent, offset)

class IntegerFeedbackState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.resolution, self.min_value, self.max_value,) = unpack_from('BBHIii', parent, offset)

class StringFeedbackState(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.class_id, self.feedback_id, self.len, self.max_symbols, self.num_keysyms,) = unpack_from('BBHHH', parent, offset)
        offset += 8
        self.keysyms = xcb.List(parent, offset, self.num_keysyms, 'I', 4)
        offset += len(self.keysyms.buf())
        xcb._resize_obj(self, offset - base)

class BellFeedbackState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.percent, self.pitch, self.duration,) = unpack_from('BBHB3xHH', parent, offset)

class LedFeedbackState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.led_mask, self.led_values,) = unpack_from('BBHII', parent, offset)

class FeedbackState(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.class_id, self.feedback_id, self.len,) = unpack_from('BBH', parent, offset)
        offset += 4
        self.uninterpreted_data = xcb.List(parent, offset, (self.len - 4), 'B', 1)
        offset += len(self.uninterpreted_data.buf())
        xcb._resize_obj(self, offset - base)

class GetFeedbackControlCookie(xcb.Cookie):
    pass

class GetFeedbackControlReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_feedbacks,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.feedbacks = xcb.List(parent, offset, self.num_feedbacks, FeedbackState, -1)

class KbdFeedbackCtl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.key, self.auto_repeat_mode, self.key_click_percent, self.bell_percent, self.bell_pitch, self.bell_duration, self.led_mask, self.led_values,) = unpack_from('BBHBBbbhhII', parent, offset)

class PtrFeedbackCtl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.num, self.denom, self.threshold,) = unpack_from('BBH2xhhh', parent, offset)

class IntegerFeedbackCtl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.int_to_display,) = unpack_from('BBHi', parent, offset)

class StringFeedbackCtl(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.class_id, self.feedback_id, self.len, self.num_keysyms,) = unpack_from('BBH2xH', parent, offset)
        offset += 8
        self.keysyms = xcb.List(parent, offset, self.num_keysyms, 'I', 4)
        offset += len(self.keysyms.buf())
        xcb._resize_obj(self, offset - base)

class BellFeedbackCtl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.percent, self.pitch, self.duration,) = unpack_from('BBHb3xhh', parent, offset)

class LedFeedbackCtl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.feedback_id, self.len, self.led_mask, self.led_values,) = unpack_from('BBHII', parent, offset)

class FeedbackCtl(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.class_id, self.feedback_id, self.len,) = unpack_from('BBH', parent, offset)
        offset += 4
        self.uninterpreted_data = xcb.List(parent, offset, (self.len - 4), 'B', 1)
        offset += len(self.uninterpreted_data.buf())
        xcb._resize_obj(self, offset - base)

class GetDeviceKeyMappingCookie(xcb.Cookie):
    pass

class GetDeviceKeyMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.keysyms_per_keycode,) = unpack_from('xx2x4xB23x', parent, offset)
        offset += 32
        self.keysyms = xcb.List(parent, offset, self.length, 'I', 4)

class GetDeviceModifierMappingCookie(xcb.Cookie):
    pass

class GetDeviceModifierMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.keycodes_per_modifier,) = unpack_from('xx2x4xB23x', parent, offset)
        offset += 32
        self.keymaps = xcb.List(parent, offset, (self.keycodes_per_modifier * 8), 'B', 1)

class SetDeviceModifierMappingCookie(xcb.Cookie):
    pass

class SetDeviceModifierMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class GetDeviceButtonMappingCookie(xcb.Cookie):
    pass

class GetDeviceButtonMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.map_size,) = unpack_from('xx2x4xB23x', parent, offset)
        offset += 32
        self.map = xcb.List(parent, offset, self.map_size, 'B', 1)

class SetDeviceButtonMappingCookie(xcb.Cookie):
    pass

class SetDeviceButtonMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class KeyState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.len, self.num_keys,) = unpack_from('BBBx', parent, offset)
        offset += 4
        self.keys = xcb.List(parent, offset, 32, 'B', 1)

class ButtonState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.class_id, self.len, self.num_buttons,) = unpack_from('BBBx', parent, offset)
        offset += 4
        self.buttons = xcb.List(parent, offset, 32, 'B', 1)

class ValuatorState(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.class_id, self.len, self.num_valuators, self.mode,) = unpack_from('BBBB', parent, offset)
        offset += 4
        self.valuators = xcb.List(parent, offset, self.num_valuators, 'I', 4)
        offset += len(self.valuators.buf())
        xcb._resize_obj(self, offset - base)

class InputState(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.class_id, self.len, self.num_items,) = unpack_from('BBBx', parent, offset)
        offset += 4
        self.uninterpreted_data = xcb.List(parent, offset, (self.len - 4), 'B', 1)
        offset += len(self.uninterpreted_data.buf())
        xcb._resize_obj(self, offset - base)

class QueryDeviceStateCookie(xcb.Cookie):
    pass

class QueryDeviceStateReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_classes,) = unpack_from('xx2x4xB23x', parent, offset)
        offset += 32
        self.classes = xcb.List(parent, offset, self.num_classes, InputState, -1)

class SetDeviceValuatorsCookie(xcb.Cookie):
    pass

class SetDeviceValuatorsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class DeviceControl:
    resolution = 1
    abs_calib = 2
    core = 3
    enable = 4
    abs_area = 5

class DeviceResolutionState(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.control_id, self.len, self.num_valuators,) = unpack_from('HHI', parent, offset)
        offset += 8
        self.resolution_values = xcb.List(parent, offset, self.num_valuators, 'I', 4)
        offset += len(self.resolution_values.buf())
        offset += xcb.type_pad(4, offset)
        self.resolution_min = xcb.List(parent, offset, self.num_valuators, 'I', 4)
        offset += len(self.resolution_min.buf())
        offset += xcb.type_pad(4, offset)
        self.resolution_max = xcb.List(parent, offset, self.num_valuators, 'I', 4)
        offset += len(self.resolution_max.buf())
        xcb._resize_obj(self, offset - base)

class DeviceAbsCalibState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.control_id, self.len, self.min_x, self.max_x, self.min_y, self.max_y, self.flip_x, self.flip_y, self.rotation, self.button_threshold,) = unpack_from('HHiiiiIIII', parent, offset)

class DeviceAbsAreaState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.control_id, self.len, self.offset_x, self.offset_y, self.width, self.height, self.screen, self.following,) = unpack_from('HHIIIIII', parent, offset)

class DeviceCoreState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.control_id, self.len, self.status, self.iscore,) = unpack_from('HHBB2x', parent, offset)

class DeviceEnableState(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.control_id, self.len, self.enable,) = unpack_from('HHB3x', parent, offset)

class DeviceState(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.control_id, self.len,) = unpack_from('HH', parent, offset)
        offset += 4
        self.uninterpreted_data = xcb.List(parent, offset, (self.len - 4), 'B', 1)
        offset += len(self.uninterpreted_data.buf())
        xcb._resize_obj(self, offset - base)

class GetDeviceControlCookie(xcb.Cookie):
    pass

class GetDeviceControlReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)
        offset += 32
        self.control = DeviceState(parent, offset)

class DeviceResolutionCtl(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.control_id, self.len, self.first_valuator, self.num_valuators,) = unpack_from('HHBB', parent, offset)
        offset += 6
        self.resolution_values = xcb.List(parent, offset, self.num_valuators, 'I', 4)
        offset += len(self.resolution_values.buf())
        xcb._resize_obj(self, offset - base)

class DeviceAbsCalibCtl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.control_id, self.len, self.min_x, self.max_x, self.min_y, self.max_y, self.flip_x, self.flip_y, self.rotation, self.button_threshold,) = unpack_from('HHiiiiIIII', parent, offset)

class DeviceAbsAreaCtrl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.control_id, self.len, self.offset_x, self.offset_y, self.width, self.height, self.screen, self.following,) = unpack_from('HHIIiiiI', parent, offset)

class DeviceCoreCtrl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.control_id, self.len, self.status,) = unpack_from('HHB3x', parent, offset)

class DeviceEnableCtrl(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.control_id, self.len, self.enable,) = unpack_from('HHB3x', parent, offset)

class DeviceCtl(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.control_id, self.len,) = unpack_from('HH', parent, offset)
        offset += 4
        self.uninterpreted_data = xcb.List(parent, offset, (self.len - 4), 'B', 1)
        offset += len(self.uninterpreted_data.buf())
        xcb._resize_obj(self, offset - base)

class ChangeDeviceControlCookie(xcb.Cookie):
    pass

class ChangeDeviceControlReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class ListDevicePropertiesCookie(xcb.Cookie):
    pass

class ListDevicePropertiesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_atoms,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.atoms = xcb.List(parent, offset, self.num_atoms, 'I', 4)

class PropertyFormat:
    _8Bits =  8
    _16Bits = 16
    _32Bits = 32

class GetDevicePropertyCookie(xcb.Cookie):
    pass

class GetDevicePropertyReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.type, self.bytes_after, self.num_items, self.format, self.device_id,) = unpack_from('xx2x4xIIIBB10x', parent, offset)
        offset += 32
        self.items = items(parent, offset)

class Device:
    All = 0
    AllMaster = 1

class GroupInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.base, self.latched, self.locked, self.effective,) = unpack_from('BBBB', parent, offset)

class ModifierInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.base, self.latched, self.locked, self.effective,) = unpack_from('IIII', parent, offset)

class XIQueryPointerCookie(xcb.Cookie):
    pass

class XIQueryPointerReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.root, self.child, self.root_x, self.root_y, self.win_x, self.win_y, self.same_screen, self.buttons_len,) = unpack_from('xx2x4xIIiiiiBxH', parent, offset)
        offset += 36
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.buttons = xcb.List(parent, offset, self.buttons_len, 'I', 4)

class HierarchyChangeType:
    AddMaster = 1
    RemoveMaster = 2
    AttachSlave = 3
    DetachSlave = 4

class ChangeMode:
    Attach = 1
    Float = 2

class AddMaster(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.type, self.len, self.name_len, self.send_core, self.enable,) = unpack_from('HHHBB', parent, offset)
        offset += 8
        self.name = xcb.List(parent, offset, self.name_len, 'b', 1)
        offset += len(self.name.buf())
        xcb._resize_obj(self, offset - base)

class RemoveMaster(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.type, self.len, self.deviceid, self.return_mode, self.return_pointer, self.return_keyboard,) = unpack_from('HHHBxHH', parent, offset)

class AttachSlave(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.type, self.len, self.deviceid, self.master,) = unpack_from('HHHH', parent, offset)

class DetachSlave(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.type, self.len, self.deviceid,) = unpack_from('HHH2x', parent, offset)

class HierarchyChange(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.type, self.len,) = unpack_from('HH', parent, offset)
        offset += 4
        self.uninterpreted_data = xcb.List(parent, offset, ((self.len * 4) - 4), 'B', 1)
        offset += len(self.uninterpreted_data.buf())
        xcb._resize_obj(self, offset - base)

class XIGetClientPointerCookie(xcb.Cookie):
    pass

class XIGetClientPointerReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.set, self.deviceid,) = unpack_from('xx2x4xBxH20x', parent, offset)

class XIEventMask:
    DeviceChanged = 2
    KeyPress = 4
    KeyRelease = 8
    ButtonPress = 16
    ButtonRelease = 32
    Motion = 64
    Enter = 128
    Leave = 256
    FocusIn = 512
    FocusOut = 1024
    Hierarchy = 2048
    Property = 4096
    RawKeyPress = 8192
    RawKeyRelease = 16384
    RawButtonPress = 32768
    RawButtonRelease = 65536
    RawMotion = 131072
    TouchBegin = 262144
    TouchUpdate = 524288
    TouchEnd = 1048576
    TouchOwnership = 2097152
    RawTouchBegin = 4194304
    RawTouchUpdate = 8388608
    RawTouchEnd = 16777216
    BarrierHit = 33554432
    BarrierLeave = 67108864

class EventMask(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.deviceid, self.mask_len,) = unpack_from('HH', parent, offset)
        offset += 4
        self.mask = xcb.List(parent, offset, self.mask_len, 'I', 4)
        offset += len(self.mask.buf())
        xcb._resize_obj(self, offset - base)

class XIQueryVersionCookie(xcb.Cookie):
    pass

class XIQueryVersionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.major_version, self.minor_version,) = unpack_from('xx2x4xHH20x', parent, offset)

class DeviceClassType:
    Key = 0
    Button = 1
    Valuator = 2
    Scroll = 3
    Touch = 8

class DeviceType:
    MasterPointer = 1
    MasterKeyboard = 2
    SlavePointer = 3
    SlaveKeyboard = 4
    FloatingSlave = 5

class ScrollFlags:
    NoEmulation = 1
    Preferred = 2

class ScrollType:
    Vertical = 1
    Horizontal = 2

class TouchMode:
    Direct = 1
    Dependent = 2

class ButtonClass(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.type, self.len, self.sourceid, self.num_buttons,) = unpack_from('HHHH', parent, offset)
        offset += 8
        self.state = xcb.List(parent, offset, ((self.num_buttons + 31) / 32), 'I', 4)
        offset += len(self.state.buf())
        offset += xcb.type_pad(4, offset)
        self.labels = xcb.List(parent, offset, self.num_buttons, 'I', 4)
        offset += len(self.labels.buf())
        xcb._resize_obj(self, offset - base)

class KeyClass(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.type, self.len, self.sourceid, self.num_keys,) = unpack_from('HHHH', parent, offset)
        offset += 8
        self.keys = xcb.List(parent, offset, self.num_keys, 'I', 4)
        offset += len(self.keys.buf())
        xcb._resize_obj(self, offset - base)

class ScrollClass(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.type, self.len, self.sourceid, self.number, self.scroll_type, self.flags,) = unpack_from('HHHHH2xI', parent, offset)
        offset += 16
        self.increment = input.FP3232(parent, offset, 8)

class TouchClass(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.type, self.len, self.sourceid, self.mode, self.num_touches,) = unpack_from('HHHBB', parent, offset)

class ValuatorClass(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.type, self.len, self.sourceid, self.number, self.label,) = unpack_from('HHHHI', parent, offset)
        offset += 12
        self.min = input.FP3232(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.max = input.FP3232(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.value = input.FP3232(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(4, offset)
        (self.resolution, self.mode,) = unpack_from('IB3x', parent, offset)

class DeviceClass(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.type, self.len, self.sourceid,) = unpack_from('HHH2x', parent, offset)
        offset += 8
        self.uninterpreted_data = xcb.List(parent, offset, ((self.len * 4) - 8), 'B', 1)
        offset += len(self.uninterpreted_data.buf())
        xcb._resize_obj(self, offset - base)

class XIDeviceInfo(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.deviceid, self.type, self.attachment, self.num_classes, self.name_len, self.enabled,) = unpack_from('HHHHHBx', parent, offset)
        offset += 12
        self.name = xcb.List(parent, offset, (((self.name_len + 3) / 4) * 4), 'b', 1)
        offset += len(self.name.buf())
        offset += xcb.type_pad(4, offset)
        self.classes = xcb.List(parent, offset, self.num_classes, DeviceClass, -1)
        offset += len(self.classes.buf())
        xcb._resize_obj(self, offset - base)

class XIQueryDeviceCookie(xcb.Cookie):
    pass

class XIQueryDeviceReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_infos,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.infos = xcb.List(parent, offset, self.num_infos, XIDeviceInfo, -1)

class XIGetFocusCookie(xcb.Cookie):
    pass

class XIGetFocusReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.focus,) = unpack_from('xx2x4xI20x', parent, offset)

class GrabOwner:
    NoOwner = 0
    Owner = 1

class XIGrabDeviceCookie(xcb.Cookie):
    pass

class XIGrabDeviceReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = unpack_from('xx2x4xB23x', parent, offset)

class EventMode:
    AsyncDevice = 0
    SyncDevice = 1
    ReplayDevice = 2
    AsyncPairedDevice = 3
    AsyncPair = 4
    SyncPair = 5
    AcceptTouch = 6
    RejectTouch = 7

class GrabMode22:
    Sync = 0
    Async = 1
    Touch = 2

class GrabType:
    Button = 0
    Keycode = 1
    Enter = 2
    FocusIn = 3
    TouchBegin = 4

class ModifierMask:
    Any = 2147483648

class GrabModifierInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.modifiers, self.status,) = unpack_from('IB3x', parent, offset)

class XIPassiveGrabDeviceCookie(xcb.Cookie):
    pass

class XIPassiveGrabDeviceReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_modifiers,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.modifiers = xcb.List(parent, offset, self.num_modifiers, GrabModifierInfo, 8)

class XIListPropertiesCookie(xcb.Cookie):
    pass

class XIListPropertiesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_properties,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.properties = xcb.List(parent, offset, self.num_properties, 'I', 4)

class XIGetPropertyCookie(xcb.Cookie):
    pass

class XIGetPropertyReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.type, self.bytes_after, self.num_items, self.format,) = unpack_from('xx2x4xIIIB11x', parent, offset)
        offset += 32
        self.items = items(parent, offset)

class XIGetSelectedEventsCookie(xcb.Cookie):
    pass

class XIGetSelectedEventsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_masks,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.masks = xcb.List(parent, offset, self.num_masks, EventMask, -1)

class BarrierReleasePointerInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.deviceid, self.barrier, self.eventid,) = unpack_from('H2xII', parent, offset)

class DeviceValuatorEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.device_id, self.device_state, self.num_valuators, self.first_valuator,) = unpack_from('xB2xHBB', parent, offset)
        offset += 8
        self.valuators = xcb.List(parent, offset, 6, 'i', 4)

class DeviceKeyPressEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen, self.device_id,) = unpack_from('xB2xIIIIhhhhHBB', parent, offset)

class DeviceKeyReleaseEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen, self.device_id,) = unpack_from('xB2xIIIIhhhhHBB', parent, offset)

class DeviceButtonPressEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen, self.device_id,) = unpack_from('xB2xIIIIhhhhHBB', parent, offset)

class DeviceButtonReleaseEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen, self.device_id,) = unpack_from('xB2xIIIIhhhhHBB', parent, offset)

class DeviceMotionNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen, self.device_id,) = unpack_from('xB2xIIIIhhhhHBB', parent, offset)

class DeviceFocusInEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.window, self.mode, self.device_id,) = unpack_from('xB2xIIBB18x', parent, offset)

class DeviceFocusOutEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.window, self.mode, self.device_id,) = unpack_from('xB2xIIBB18x', parent, offset)

class ProximityInEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen, self.device_id,) = unpack_from('xB2xIIIIhhhhHBB', parent, offset)

class ProximityOutEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.detail, self.time, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen, self.device_id,) = unpack_from('xB2xIIIIhhhhHBB', parent, offset)

class DeviceStateNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.device_id, self.time, self.num_keys, self.num_buttons, self.num_valuators, self.classes_reported,) = unpack_from('xB2xIBBBB', parent, offset)
        offset += 12
        self.buttons = xcb.List(parent, offset, 4, 'B', 1)
        offset += len(self.buttons.buf())
        offset += xcb.type_pad(1, offset)
        self.keys = xcb.List(parent, offset, 4, 'B', 1)
        offset += len(self.keys.buf())
        offset += xcb.type_pad(4, offset)
        self.valuators = xcb.List(parent, offset, 3, 'I', 4)

class DeviceMappingNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.device_id, self.request, self.first_keycode, self.count, self.time,) = unpack_from('xB2xBBBxI20x', parent, offset)

class ChangeDeviceNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.device_id, self.time, self.request,) = unpack_from('xB2xIB23x', parent, offset)

class DeviceKeyStateNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.device_id,) = unpack_from('xB2x', parent, offset)
        offset += 4
        self.keys = xcb.List(parent, offset, 28, 'B', 1)

class DeviceButtonStateNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.device_id,) = unpack_from('xB2x', parent, offset)
        offset += 4
        self.buttons = xcb.List(parent, offset, 28, 'B', 1)

class DeviceChange:
    Added = 0
    Removed = 1
    Enabled = 2
    Disabled = 3
    Unrecoverable = 4
    ControlChanged = 5

class DevicePresenceNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.time, self.devchange, self.device_id, self.control,) = unpack_from('xx2xIBBH20x', parent, offset)

class DevicePropertyNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.state, self.time, self.property, self.device_id,) = unpack_from('xB2xII19xB', parent, offset)

class ChangeReason:
    SlaveSwitch = 1
    DeviceChange = 2

class DeviceChangedEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.num_classes, self.sourceid, self.reason,) = unpack_from('xx2x4x2xHIHHB11x', parent, offset)
        offset += 32
        self.classes = xcb.List(parent, offset, self.num_classes, DeviceClass, -1)
        offset += len(self.classes.buf())

class KeyEventFlags:
    KeyRepeat = 65536

class KeyPressEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.buttons_len, self.valuators_len, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIiiiiHHH2xI', parent, offset)
        offset += 60
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.button_mask = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.button_mask.buf())
        offset += xcb.type_pad(4, offset)
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class KeyReleaseEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.buttons_len, self.valuators_len, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIiiiiHHH2xI', parent, offset)
        offset += 60
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.button_mask = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.button_mask.buf())
        offset += xcb.type_pad(4, offset)
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class PointerEventFlags:
    PointerEmulated = 65536

class ButtonPressEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.buttons_len, self.valuators_len, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIiiiiHHH2xI', parent, offset)
        offset += 60
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.button_mask = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.button_mask.buf())
        offset += xcb.type_pad(4, offset)
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class ButtonReleaseEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.buttons_len, self.valuators_len, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIiiiiHHH2xI', parent, offset)
        offset += 60
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.button_mask = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.button_mask.buf())
        offset += xcb.type_pad(4, offset)
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class MotionEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.buttons_len, self.valuators_len, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIiiiiHHH2xI', parent, offset)
        offset += 60
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.button_mask = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.button_mask.buf())
        offset += xcb.type_pad(4, offset)
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class NotifyMode:
    Normal = 0
    Grab = 1
    Ungrab = 2
    WhileGrabbed = 3
    PassiveGrab = 4
    PassiveUngrab = 5

class NotifyDetail:
    Ancestor = 0
    Virtual = 1
    Inferior = 2
    Nonlinear = 3
    NonlinearVirtual = 4
    Pointer = 5
    PointerRoot = 6
    _None = 7

class EnterEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.sourceid, self.mode, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.same_screen, self.focus, self.buttons_len,) = unpack_from('xx2x4x2xHIHBBIIIiiiiBBH', parent, offset)
        offset += 52
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.buttons = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.buttons.buf())

class LeaveEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.sourceid, self.mode, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.same_screen, self.focus, self.buttons_len,) = unpack_from('xx2x4x2xHIHBBIIIiiiiBBH', parent, offset)
        offset += 52
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.buttons = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.buttons.buf())

class FocusInEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.sourceid, self.mode, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.same_screen, self.focus, self.buttons_len,) = unpack_from('xx2x4x2xHIHBBIIIiiiiBBH', parent, offset)
        offset += 52
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.buttons = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.buttons.buf())

class FocusOutEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.sourceid, self.mode, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.same_screen, self.focus, self.buttons_len,) = unpack_from('xx2x4x2xHIHBBIIIiiiiBBH', parent, offset)
        offset += 52
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.buttons = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.buttons.buf())

class HierarchyMask:
    MasterAdded = 1
    MasterRemoved = 2
    SlaveAdded = 4
    SlaveRemoved = 8
    SlaveAttached = 16
    SlaveDetached = 32
    DeviceEnabled = 64
    DeviceDisabled = 128

class HierarchyInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.deviceid, self.attachment, self.type, self.enabled, self.flags,) = unpack_from('HHBB2xI', parent, offset)

class HierarchyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.flags, self.num_infos,) = unpack_from('xx2x4x2xHIIH10x', parent, offset)
        offset += 32
        self.infos = xcb.List(parent, offset, self.num_infos, HierarchyInfo, 12)
        offset += len(self.infos.buf())

class PropertyFlag:
    Deleted = 0
    Created = 1
    Modified = 2

class PropertyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.property, self.what,) = unpack_from('xx2x4x2xHIIB11x', parent, offset)

class RawKeyPressEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.sourceid, self.valuators_len, self.flags,) = unpack_from('xx2x4x2xHIIHHI4x', parent, offset)
        offset += 32
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class RawKeyReleaseEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.sourceid, self.valuators_len, self.flags,) = unpack_from('xx2x4x2xHIIHHI4x', parent, offset)
        offset += 32
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class RawButtonPressEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.sourceid, self.valuators_len, self.flags,) = unpack_from('xx2x4x2xHIIHHI4x', parent, offset)
        offset += 32
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class RawButtonReleaseEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.sourceid, self.valuators_len, self.flags,) = unpack_from('xx2x4x2xHIIHHI4x', parent, offset)
        offset += 32
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class RawMotionEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.sourceid, self.valuators_len, self.flags,) = unpack_from('xx2x4x2xHIIHHI4x', parent, offset)
        offset += 32
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class TouchEventFlags:
    TouchPendingEnd = 65536
    TouchEmulatingPointer = 131072

class TouchBeginEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.buttons_len, self.valuators_len, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIiiiiHHH2xI', parent, offset)
        offset += 60
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.button_mask = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.button_mask.buf())
        offset += xcb.type_pad(4, offset)
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class TouchUpdateEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.buttons_len, self.valuators_len, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIiiiiHHH2xI', parent, offset)
        offset += 60
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.button_mask = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.button_mask.buf())
        offset += xcb.type_pad(4, offset)
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class TouchEndEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.root, self.event, self.child, self.root_x, self.root_y, self.event_x, self.event_y, self.buttons_len, self.valuators_len, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIiiiiHHH2xI', parent, offset)
        offset += 60
        self.mods = input.ModifierInfo(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        self.group = input.GroupInfo(parent, offset, 4)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.button_mask = xcb.List(parent, offset, self.buttons_len, 'I', 4)
        offset += len(self.button_mask.buf())
        offset += xcb.type_pad(4, offset)
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class TouchOwnershipFlags:
    _None = 0

class TouchOwnershipEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.touchid, self.root, self.event, self.child, self.sourceid, self.flags,) = unpack_from('xx2x4x2xHIIIIIH2xI8x', parent, offset)

class RawTouchBeginEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.sourceid, self.valuators_len, self.flags,) = unpack_from('xx2x4x2xHIIHHI4x', parent, offset)
        offset += 32
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class RawTouchUpdateEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.sourceid, self.valuators_len, self.flags,) = unpack_from('xx2x4x2xHIIHHI4x', parent, offset)
        offset += 32
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class RawTouchEndEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.detail, self.sourceid, self.valuators_len, self.flags,) = unpack_from('xx2x4x2xHIIHHI4x', parent, offset)
        offset += 32
        self.valuator_mask = xcb.List(parent, offset, self.valuators_len, 'I', 4)
        offset += len(self.valuator_mask.buf())

class BarrierHitEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.eventid, self.root, self.event, self.barrier, self.dtime, self.flags, self.sourceid, self.root_x, self.root_y,) = unpack_from('xx2x4x2xHIIIIIIIH2xii', parent, offset)
        offset += 52
        self.dx = input.FP3232(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.dy = input.FP3232(parent, offset, 8)

class BarrierLeaveEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.deviceid, self.time, self.eventid, self.root, self.event, self.barrier, self.dtime, self.flags, self.sourceid, self.root_x, self.root_y,) = unpack_from('xx2x4x2xHIIIIIIIH2xii', parent, offset)
        offset += 52
        self.dx = input.FP3232(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.dy = input.FP3232(parent, offset, 8)

class DeviceError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadDevice(xcb.ProtocolException):
    pass

class EventError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadEvent(xcb.ProtocolException):
    pass

class ModeError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadMode(xcb.ProtocolException):
    pass

class DeviceBusyError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadDeviceBusy(xcb.ProtocolException):
    pass

class ClassError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadClass(xcb.ProtocolException):
    pass

class xinputExtension(xcb.Extension):

    def GetExtensionVersion(self, name_len, name):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2x', name_len))
        buf.write(str(buffer(array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, True),
                                 GetExtensionVersionCookie(),
                                 GetExtensionVersionReply)

    def GetExtensionVersionUnchecked(self, name_len, name):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2x', name_len))
        buf.write(str(buffer(array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, False),
                                 GetExtensionVersionCookie(),
                                 GetExtensionVersionReply)

    def ListInputDevices(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, True),
                                 ListInputDevicesCookie(),
                                 ListInputDevicesReply)

    def ListInputDevicesUnchecked(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, False),
                                 ListInputDevicesCookie(),
                                 ListInputDevicesReply)

    def OpenDevice(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 3, False, True),
                                 OpenDeviceCookie(),
                                 OpenDeviceReply)

    def OpenDeviceUnchecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 3, False, False),
                                 OpenDeviceCookie(),
                                 OpenDeviceReply)

    def CloseDeviceChecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, True),
                                 xcb.VoidCookie())

    def CloseDevice(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, False),
                                 xcb.VoidCookie())

    def SetDeviceMode(self, device_id, mode):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBB2x', device_id, mode))
        return self.send_request(xcb.Request(buf.getvalue(), 5, False, True),
                                 SetDeviceModeCookie(),
                                 SetDeviceModeReply)

    def SetDeviceModeUnchecked(self, device_id, mode):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBB2x', device_id, mode))
        return self.send_request(xcb.Request(buf.getvalue(), 5, False, False),
                                 SetDeviceModeCookie(),
                                 SetDeviceModeReply)

    def SelectExtensionEventChecked(self, window, num_classes, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, num_classes))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, True),
                                 xcb.VoidCookie())

    def SelectExtensionEvent(self, window, num_classes, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, num_classes))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, False),
                                 xcb.VoidCookie())

    def GetSelectedExtensionEvents(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 7, False, True),
                                 GetSelectedExtensionEventsCookie(),
                                 GetSelectedExtensionEventsReply)

    def GetSelectedExtensionEventsUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 7, False, False),
                                 GetSelectedExtensionEventsCookie(),
                                 GetSelectedExtensionEventsReply)

    def ChangeDeviceDontPropagateListChecked(self, window, num_classes, mode, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHBx', window, num_classes, mode))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, True),
                                 xcb.VoidCookie())

    def ChangeDeviceDontPropagateList(self, window, num_classes, mode, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHBx', window, num_classes, mode))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, False),
                                 xcb.VoidCookie())

    def GetDeviceDontPropagateList(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 9, False, True),
                                 GetDeviceDontPropagateListCookie(),
                                 GetDeviceDontPropagateListReply)

    def GetDeviceDontPropagateListUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 9, False, False),
                                 GetDeviceDontPropagateListCookie(),
                                 GetDeviceDontPropagateListReply)

    def GetDeviceMotionEvents(self, start, stop, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIB', start, stop, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 10, False, True),
                                 GetDeviceMotionEventsCookie(),
                                 GetDeviceMotionEventsReply)

    def GetDeviceMotionEventsUnchecked(self, start, stop, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIB', start, stop, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 10, False, False),
                                 GetDeviceMotionEventsCookie(),
                                 GetDeviceMotionEventsReply)

    def ChangeKeyboardDevice(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 11, False, True),
                                 ChangeKeyboardDeviceCookie(),
                                 ChangeKeyboardDeviceReply)

    def ChangeKeyboardDeviceUnchecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 11, False, False),
                                 ChangeKeyboardDeviceCookie(),
                                 ChangeKeyboardDeviceReply)

    def ChangePointerDevice(self, x_axis, y_axis, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBBx', x_axis, y_axis, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 12, False, True),
                                 ChangePointerDeviceCookie(),
                                 ChangePointerDeviceReply)

    def ChangePointerDeviceUnchecked(self, x_axis, y_axis, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBBx', x_axis, y_axis, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 12, False, False),
                                 ChangePointerDeviceCookie(),
                                 ChangePointerDeviceReply)

    def GrabDevice(self, grab_window, time, num_classes, this_device_mode, other_device_mode, owner_events, device_id, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHBBBB2x', grab_window, time, num_classes, this_device_mode, other_device_mode, owner_events, device_id))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 13, False, True),
                                 GrabDeviceCookie(),
                                 GrabDeviceReply)

    def GrabDeviceUnchecked(self, grab_window, time, num_classes, this_device_mode, other_device_mode, owner_events, device_id, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHBBBB2x', grab_window, time, num_classes, this_device_mode, other_device_mode, owner_events, device_id))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 13, False, False),
                                 GrabDeviceCookie(),
                                 GrabDeviceReply)

    def UngrabDeviceChecked(self, time, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB', time, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 14, True, True),
                                 xcb.VoidCookie())

    def UngrabDevice(self, time, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB', time, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 14, True, False),
                                 xcb.VoidCookie())

    def GrabDeviceKeyChecked(self, grab_window, num_classes, modifiers, modifier_device, grabbed_device, key, this_device_mode, other_device_mode, owner_events, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHHBBBBBB2x', grab_window, num_classes, modifiers, modifier_device, grabbed_device, key, this_device_mode, other_device_mode, owner_events))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 15, True, True),
                                 xcb.VoidCookie())

    def GrabDeviceKey(self, grab_window, num_classes, modifiers, modifier_device, grabbed_device, key, this_device_mode, other_device_mode, owner_events, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHHBBBBBB2x', grab_window, num_classes, modifiers, modifier_device, grabbed_device, key, this_device_mode, other_device_mode, owner_events))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 15, True, False),
                                 xcb.VoidCookie())

    def UngrabDeviceKeyChecked(self, grabWindow, modifiers, modifier_device, key, grabbed_device):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHBBB', grabWindow, modifiers, modifier_device, key, grabbed_device))
        return self.send_request(xcb.Request(buf.getvalue(), 16, True, True),
                                 xcb.VoidCookie())

    def UngrabDeviceKey(self, grabWindow, modifiers, modifier_device, key, grabbed_device):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHBBB', grabWindow, modifiers, modifier_device, key, grabbed_device))
        return self.send_request(xcb.Request(buf.getvalue(), 16, True, False),
                                 xcb.VoidCookie())

    def GrabDeviceButtonChecked(self, grab_window, grabbed_device, modifier_device, num_classes, modifiers, this_device_mode, other_device_mode, button, owner_events, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIBBHHBBBB2x', grab_window, grabbed_device, modifier_device, num_classes, modifiers, this_device_mode, other_device_mode, button, owner_events))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, True),
                                 xcb.VoidCookie())

    def GrabDeviceButton(self, grab_window, grabbed_device, modifier_device, num_classes, modifiers, this_device_mode, other_device_mode, button, owner_events, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIBBHHBBBB2x', grab_window, grabbed_device, modifier_device, num_classes, modifiers, this_device_mode, other_device_mode, button, owner_events))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, False),
                                 xcb.VoidCookie())

    def UngrabDeviceButtonChecked(self, grab_window, modifiers, modifier_device, button, grabbed_device):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHBBB', grab_window, modifiers, modifier_device, button, grabbed_device))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, True),
                                 xcb.VoidCookie())

    def UngrabDeviceButton(self, grab_window, modifiers, modifier_device, button, grabbed_device):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHBBB', grab_window, modifiers, modifier_device, button, grabbed_device))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, False),
                                 xcb.VoidCookie())

    def AllowDeviceEventsChecked(self, time, mode, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIBB', time, mode, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, True),
                                 xcb.VoidCookie())

    def AllowDeviceEvents(self, time, mode, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIBB', time, mode, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, False),
                                 xcb.VoidCookie())

    def GetDeviceFocus(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 20, False, True),
                                 GetDeviceFocusCookie(),
                                 GetDeviceFocusReply)

    def GetDeviceFocusUnchecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 20, False, False),
                                 GetDeviceFocusCookie(),
                                 GetDeviceFocusReply)

    def SetDeviceFocusChecked(self, focus, time, revert_to, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIBB', focus, time, revert_to, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 21, True, True),
                                 xcb.VoidCookie())

    def SetDeviceFocus(self, focus, time, revert_to, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIBB', focus, time, revert_to, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 21, True, False),
                                 xcb.VoidCookie())

    def GetFeedbackControl(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 22, False, True),
                                 GetFeedbackControlCookie(),
                                 GetFeedbackControlReply)

    def GetFeedbackControlUnchecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 22, False, False),
                                 GetFeedbackControlCookie(),
                                 GetFeedbackControlReply)

    def ChangeFeedbackControlChecked(self, mask, device_id, feedback_id, feedback):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIBB', mask, device_id, feedback_id))
        for elt in xcb.Iterator(feedback, -1, 'feedback', False):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 23, True, True),
                                 xcb.VoidCookie())

    def ChangeFeedbackControl(self, mask, device_id, feedback_id, feedback):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIBB', mask, device_id, feedback_id))
        for elt in xcb.Iterator(feedback, -1, 'feedback', False):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 23, True, False),
                                 xcb.VoidCookie())

    def GetDeviceKeyMapping(self, device_id, first_keycode, count):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBB', device_id, first_keycode, count))
        return self.send_request(xcb.Request(buf.getvalue(), 24, False, True),
                                 GetDeviceKeyMappingCookie(),
                                 GetDeviceKeyMappingReply)

    def GetDeviceKeyMappingUnchecked(self, device_id, first_keycode, count):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBB', device_id, first_keycode, count))
        return self.send_request(xcb.Request(buf.getvalue(), 24, False, False),
                                 GetDeviceKeyMappingCookie(),
                                 GetDeviceKeyMappingReply)

    def ChangeDeviceKeyMappingChecked(self, device_id, first_keycode, keysyms_per_keycode, keycode_count, keysyms):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBBB', device_id, first_keycode, keysyms_per_keycode, keycode_count))
        buf.write(str(buffer(array('I', keysyms))))
        return self.send_request(xcb.Request(buf.getvalue(), 25, True, True),
                                 xcb.VoidCookie())

    def ChangeDeviceKeyMapping(self, device_id, first_keycode, keysyms_per_keycode, keycode_count, keysyms):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBBB', device_id, first_keycode, keysyms_per_keycode, keycode_count))
        buf.write(str(buffer(array('I', keysyms))))
        return self.send_request(xcb.Request(buf.getvalue(), 25, True, False),
                                 xcb.VoidCookie())

    def GetDeviceModifierMapping(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 26, False, True),
                                 GetDeviceModifierMappingCookie(),
                                 GetDeviceModifierMappingReply)

    def GetDeviceModifierMappingUnchecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 26, False, False),
                                 GetDeviceModifierMappingCookie(),
                                 GetDeviceModifierMappingReply)

    def SetDeviceModifierMapping(self, device_id, keycodes_per_modifier, keymaps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBx', device_id, keycodes_per_modifier))
        buf.write(str(buffer(array('B', keymaps))))
        return self.send_request(xcb.Request(buf.getvalue(), 27, False, True),
                                 SetDeviceModifierMappingCookie(),
                                 SetDeviceModifierMappingReply)

    def SetDeviceModifierMappingUnchecked(self, device_id, keycodes_per_modifier, keymaps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBx', device_id, keycodes_per_modifier))
        buf.write(str(buffer(array('B', keymaps))))
        return self.send_request(xcb.Request(buf.getvalue(), 27, False, False),
                                 SetDeviceModifierMappingCookie(),
                                 SetDeviceModifierMappingReply)

    def GetDeviceButtonMapping(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 28, False, True),
                                 GetDeviceButtonMappingCookie(),
                                 GetDeviceButtonMappingReply)

    def GetDeviceButtonMappingUnchecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 28, False, False),
                                 GetDeviceButtonMappingCookie(),
                                 GetDeviceButtonMappingReply)

    def SetDeviceButtonMapping(self, device_id, map_size, map):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBB2x', device_id, map_size))
        buf.write(str(buffer(array('B', map))))
        return self.send_request(xcb.Request(buf.getvalue(), 29, False, True),
                                 SetDeviceButtonMappingCookie(),
                                 SetDeviceButtonMappingReply)

    def SetDeviceButtonMappingUnchecked(self, device_id, map_size, map):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBB2x', device_id, map_size))
        buf.write(str(buffer(array('B', map))))
        return self.send_request(xcb.Request(buf.getvalue(), 29, False, False),
                                 SetDeviceButtonMappingCookie(),
                                 SetDeviceButtonMappingReply)

    def QueryDeviceState(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 30, False, True),
                                 QueryDeviceStateCookie(),
                                 QueryDeviceStateReply)

    def QueryDeviceStateUnchecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 30, False, False),
                                 QueryDeviceStateCookie(),
                                 QueryDeviceStateReply)

    def SendExtensionEventChecked(self, destination, device_id, propagate, num_classes, num_events, events, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIBBHB3x', destination, device_id, propagate, num_classes, num_events))
        buf.write(str(buffer(array('B', events))))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 31, True, True),
                                 xcb.VoidCookie())

    def SendExtensionEvent(self, destination, device_id, propagate, num_classes, num_events, events, classes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIBBHB3x', destination, device_id, propagate, num_classes, num_events))
        buf.write(str(buffer(array('B', events))))
        buf.write(str(buffer(array('I', classes))))
        return self.send_request(xcb.Request(buf.getvalue(), 31, True, False),
                                 xcb.VoidCookie())

    def DeviceBellChecked(self, device_id, feedback_id, feedback_class, percent):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBBb', device_id, feedback_id, feedback_class, percent))
        return self.send_request(xcb.Request(buf.getvalue(), 32, True, True),
                                 xcb.VoidCookie())

    def DeviceBell(self, device_id, feedback_id, feedback_class, percent):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBBb', device_id, feedback_id, feedback_class, percent))
        return self.send_request(xcb.Request(buf.getvalue(), 32, True, False),
                                 xcb.VoidCookie())

    def SetDeviceValuators(self, device_id, first_valuator, num_valuators, valuators):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBBx', device_id, first_valuator, num_valuators))
        buf.write(str(buffer(array('i', valuators))))
        return self.send_request(xcb.Request(buf.getvalue(), 33, False, True),
                                 SetDeviceValuatorsCookie(),
                                 SetDeviceValuatorsReply)

    def SetDeviceValuatorsUnchecked(self, device_id, first_valuator, num_valuators, valuators):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBBBx', device_id, first_valuator, num_valuators))
        buf.write(str(buffer(array('i', valuators))))
        return self.send_request(xcb.Request(buf.getvalue(), 33, False, False),
                                 SetDeviceValuatorsCookie(),
                                 SetDeviceValuatorsReply)

    def GetDeviceControl(self, control_id, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHBx', control_id, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 34, False, True),
                                 GetDeviceControlCookie(),
                                 GetDeviceControlReply)

    def GetDeviceControlUnchecked(self, control_id, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHBx', control_id, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 34, False, False),
                                 GetDeviceControlCookie(),
                                 GetDeviceControlReply)

    def ChangeDeviceControl(self, control_id, device_id, control):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHBx', control_id, device_id))
        for elt in xcb.Iterator(control, -1, 'control', False):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 35, False, True),
                                 ChangeDeviceControlCookie(),
                                 ChangeDeviceControlReply)

    def ChangeDeviceControlUnchecked(self, control_id, device_id, control):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHBx', control_id, device_id))
        for elt in xcb.Iterator(control, -1, 'control', False):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 35, False, False),
                                 ChangeDeviceControlCookie(),
                                 ChangeDeviceControlReply)

    def ListDeviceProperties(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 36, False, True),
                                 ListDevicePropertiesCookie(),
                                 ListDevicePropertiesReply)

    def ListDevicePropertiesUnchecked(self, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3x', device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 36, False, False),
                                 ListDevicePropertiesCookie(),
                                 ListDevicePropertiesReply)

    def ChangeDevicePropertyChecked(self, property, type, device_id, format, mode, num_items, items):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIBBBxI', property, type, device_id, format, mode, num_items))
        for elt in xcb.Iterator(items, -1, 'items', False):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 37, True, True),
                                 xcb.VoidCookie())

    def ChangeDeviceProperty(self, property, type, device_id, format, mode, num_items, items):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIBBBxI', property, type, device_id, format, mode, num_items))
        for elt in xcb.Iterator(items, -1, 'items', False):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 37, True, False),
                                 xcb.VoidCookie())

    def DeleteDevicePropertyChecked(self, property, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB3x', property, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 38, True, True),
                                 xcb.VoidCookie())

    def DeleteDeviceProperty(self, property, device_id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB3x', property, device_id))
        return self.send_request(xcb.Request(buf.getvalue(), 38, True, False),
                                 xcb.VoidCookie())

    def GetDeviceProperty(self, property, type, offset, len, device_id, delete):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIBB2x', property, type, offset, len, device_id, delete))
        return self.send_request(xcb.Request(buf.getvalue(), 39, False, True),
                                 GetDevicePropertyCookie(),
                                 GetDevicePropertyReply)

    def GetDevicePropertyUnchecked(self, property, type, offset, len, device_id, delete):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIBB2x', property, type, offset, len, device_id, delete))
        return self.send_request(xcb.Request(buf.getvalue(), 39, False, False),
                                 GetDevicePropertyCookie(),
                                 GetDevicePropertyReply)

    def XIQueryPointer(self, window, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 40, False, True),
                                 XIQueryPointerCookie(),
                                 XIQueryPointerReply)

    def XIQueryPointerUnchecked(self, window, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 40, False, False),
                                 XIQueryPointerCookie(),
                                 XIQueryPointerReply)

    def XIWarpPointerChecked(self, src_win, dst_win, src_x, src_y, src_width, src_height, dst_x, dst_y, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIiiHHiiH2x', src_win, dst_win, src_x, src_y, src_width, src_height, dst_x, dst_y, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 41, True, True),
                                 xcb.VoidCookie())

    def XIWarpPointer(self, src_win, dst_win, src_x, src_y, src_width, src_height, dst_x, dst_y, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIiiHHiiH2x', src_win, dst_win, src_x, src_y, src_width, src_height, dst_x, dst_y, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 41, True, False),
                                 xcb.VoidCookie())

    def XIChangeCursorChecked(self, window, cursor, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIH2x', window, cursor, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 42, True, True),
                                 xcb.VoidCookie())

    def XIChangeCursor(self, window, cursor, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIH2x', window, cursor, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 42, True, False),
                                 xcb.VoidCookie())

    def XIChangeHierarchyChecked(self, num_changes, changes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB', num_changes))
        for elt in xcb.Iterator(changes, -1, 'changes', True):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 43, True, True),
                                 xcb.VoidCookie())

    def XIChangeHierarchy(self, num_changes, changes):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB', num_changes))
        for elt in xcb.Iterator(changes, -1, 'changes', True):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 43, True, False),
                                 xcb.VoidCookie())

    def XISetClientPointerChecked(self, window, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 44, True, True),
                                 xcb.VoidCookie())

    def XISetClientPointer(self, window, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 44, True, False),
                                 xcb.VoidCookie())

    def XIGetClientPointer(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 45, False, True),
                                 XIGetClientPointerCookie(),
                                 XIGetClientPointerReply)

    def XIGetClientPointerUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 45, False, False),
                                 XIGetClientPointerCookie(),
                                 XIGetClientPointerReply)

    def XISelectEventsChecked(self, window, num_mask, masks):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, num_mask))
        for elt in xcb.Iterator(masks, -1, 'masks', True):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 46, True, True),
                                 xcb.VoidCookie())

    def XISelectEvents(self, window, num_mask, masks):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, num_mask))
        for elt in xcb.Iterator(masks, -1, 'masks', True):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 46, True, False),
                                 xcb.VoidCookie())

    def XIQueryVersion(self, major_version, minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHH', major_version, minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 47, False, True),
                                 XIQueryVersionCookie(),
                                 XIQueryVersionReply)

    def XIQueryVersionUnchecked(self, major_version, minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHH', major_version, minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 47, False, False),
                                 XIQueryVersionCookie(),
                                 XIQueryVersionReply)

    def XIQueryDevice(self, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2x', deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 48, False, True),
                                 XIQueryDeviceCookie(),
                                 XIQueryDeviceReply)

    def XIQueryDeviceUnchecked(self, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2x', deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 48, False, False),
                                 XIQueryDeviceCookie(),
                                 XIQueryDeviceReply)

    def XISetFocusChecked(self, window, time, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIH2x', window, time, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 49, True, True),
                                 xcb.VoidCookie())

    def XISetFocus(self, window, time, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIH2x', window, time, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 49, True, False),
                                 xcb.VoidCookie())

    def XIGetFocus(self, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2x', deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 50, False, True),
                                 XIGetFocusCookie(),
                                 XIGetFocusReply)

    def XIGetFocusUnchecked(self, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2x', deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 50, False, False),
                                 XIGetFocusCookie(),
                                 XIGetFocusReply)

    def XIGrabDevice(self, window, time, cursor, deviceid, mode, paired_device_mode, owner_events, mask_len, mask):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIHBBBxH', window, time, cursor, deviceid, mode, paired_device_mode, owner_events, mask_len))
        buf.write(str(buffer(array('I', mask))))
        return self.send_request(xcb.Request(buf.getvalue(), 51, False, True),
                                 XIGrabDeviceCookie(),
                                 XIGrabDeviceReply)

    def XIGrabDeviceUnchecked(self, window, time, cursor, deviceid, mode, paired_device_mode, owner_events, mask_len, mask):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIHBBBxH', window, time, cursor, deviceid, mode, paired_device_mode, owner_events, mask_len))
        buf.write(str(buffer(array('I', mask))))
        return self.send_request(xcb.Request(buf.getvalue(), 51, False, False),
                                 XIGrabDeviceCookie(),
                                 XIGrabDeviceReply)

    def XIUngrabDeviceChecked(self, time, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', time, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 52, True, True),
                                 xcb.VoidCookie())

    def XIUngrabDevice(self, time, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', time, deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 52, True, False),
                                 xcb.VoidCookie())

    def XIAllowEventsChecked(self, time, deviceid, event_mode, touchid, grab_window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHBxII', time, deviceid, event_mode, touchid, grab_window))
        return self.send_request(xcb.Request(buf.getvalue(), 53, True, True),
                                 xcb.VoidCookie())

    def XIAllowEvents(self, time, deviceid, event_mode, touchid, grab_window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHBxII', time, deviceid, event_mode, touchid, grab_window))
        return self.send_request(xcb.Request(buf.getvalue(), 53, True, False),
                                 xcb.VoidCookie())

    def XIPassiveGrabDevice(self, time, grab_window, cursor, detail, deviceid, num_modifiers, mask_len, grab_type, grab_mode, paired_device_mode, owner_events, mask, modifiers):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIHHHBBBB2x', time, grab_window, cursor, detail, deviceid, num_modifiers, mask_len, grab_type, grab_mode, paired_device_mode, owner_events))
        buf.write(str(buffer(array('I', mask))))
        buf.write(str(buffer(array('I', modifiers))))
        return self.send_request(xcb.Request(buf.getvalue(), 54, False, True),
                                 XIPassiveGrabDeviceCookie(),
                                 XIPassiveGrabDeviceReply)

    def XIPassiveGrabDeviceUnchecked(self, time, grab_window, cursor, detail, deviceid, num_modifiers, mask_len, grab_type, grab_mode, paired_device_mode, owner_events, mask, modifiers):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIHHHBBBB2x', time, grab_window, cursor, detail, deviceid, num_modifiers, mask_len, grab_type, grab_mode, paired_device_mode, owner_events))
        buf.write(str(buffer(array('I', mask))))
        buf.write(str(buffer(array('I', modifiers))))
        return self.send_request(xcb.Request(buf.getvalue(), 54, False, False),
                                 XIPassiveGrabDeviceCookie(),
                                 XIPassiveGrabDeviceReply)

    def XIPassiveUngrabDeviceChecked(self, grab_window, detail, deviceid, num_modifiers, grab_type, modifiers):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHHB3x', grab_window, detail, deviceid, num_modifiers, grab_type))
        buf.write(str(buffer(array('I', modifiers))))
        return self.send_request(xcb.Request(buf.getvalue(), 55, True, True),
                                 xcb.VoidCookie())

    def XIPassiveUngrabDevice(self, grab_window, detail, deviceid, num_modifiers, grab_type, modifiers):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHHB3x', grab_window, detail, deviceid, num_modifiers, grab_type))
        buf.write(str(buffer(array('I', modifiers))))
        return self.send_request(xcb.Request(buf.getvalue(), 55, True, False),
                                 xcb.VoidCookie())

    def XIListProperties(self, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2x', deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 56, False, True),
                                 XIListPropertiesCookie(),
                                 XIListPropertiesReply)

    def XIListPropertiesUnchecked(self, deviceid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2x', deviceid))
        return self.send_request(xcb.Request(buf.getvalue(), 56, False, False),
                                 XIListPropertiesCookie(),
                                 XIListPropertiesReply)

    def XIChangePropertyChecked(self, deviceid, mode, format, property, type, num_items, items):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHBBIII', deviceid, mode, format, property, type, num_items))
        for elt in xcb.Iterator(items, -1, 'items', False):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 57, True, True),
                                 xcb.VoidCookie())

    def XIChangeProperty(self, deviceid, mode, format, property, type, num_items, items):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHBBIII', deviceid, mode, format, property, type, num_items))
        for elt in xcb.Iterator(items, -1, 'items', False):
            buf.write(pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 57, True, False),
                                 xcb.VoidCookie())

    def XIDeletePropertyChecked(self, deviceid, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2xI', deviceid, property))
        return self.send_request(xcb.Request(buf.getvalue(), 58, True, True),
                                 xcb.VoidCookie())

    def XIDeleteProperty(self, deviceid, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xH2xI', deviceid, property))
        return self.send_request(xcb.Request(buf.getvalue(), 58, True, False),
                                 xcb.VoidCookie())

    def XIGetProperty(self, deviceid, delete, property, type, offset, len):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHBxIIII', deviceid, delete, property, type, offset, len))
        return self.send_request(xcb.Request(buf.getvalue(), 59, False, True),
                                 XIGetPropertyCookie(),
                                 XIGetPropertyReply)

    def XIGetPropertyUnchecked(self, deviceid, delete, property, type, offset, len):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xHBxIIII', deviceid, delete, property, type, offset, len))
        return self.send_request(xcb.Request(buf.getvalue(), 59, False, False),
                                 XIGetPropertyCookie(),
                                 XIGetPropertyReply)

    def XIGetSelectedEvents(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 60, False, True),
                                 XIGetSelectedEventsCookie(),
                                 XIGetSelectedEventsReply)

    def XIGetSelectedEventsUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 60, False, False),
                                 XIGetSelectedEventsCookie(),
                                 XIGetSelectedEventsReply)

    def XIBarrierReleasePointerChecked(self, num_barriers, barriers):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', num_barriers))
        for elt in xcb.Iterator(barriers, 3, 'barriers', True):
            buf.write(pack('=H2xII', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 61, True, True),
                                 xcb.VoidCookie())

    def XIBarrierReleasePointer(self, num_barriers, barriers):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', num_barriers))
        for elt in xcb.Iterator(barriers, 3, 'barriers', True):
            buf.write(pack('=H2xII', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 61, True, False),
                                 xcb.VoidCookie())

_events = {
    0 : DeviceValuatorEvent,
    1 : DeviceKeyPressEvent,
    2 : DeviceKeyReleaseEvent,
    3 : DeviceButtonPressEvent,
    4 : DeviceButtonReleaseEvent,
    5 : DeviceMotionNotifyEvent,
    6 : DeviceFocusInEvent,
    7 : DeviceFocusOutEvent,
    8 : ProximityInEvent,
    9 : ProximityOutEvent,
    10 : DeviceStateNotifyEvent,
    11 : DeviceMappingNotifyEvent,
    12 : ChangeDeviceNotifyEvent,
    13 : DeviceKeyStateNotifyEvent,
    14 : DeviceButtonStateNotifyEvent,
    15 : DevicePresenceNotifyEvent,
    16 : DevicePropertyNotifyEvent,
    1 : DeviceChangedEvent,
    2 : KeyPressEvent,
    3 : KeyReleaseEvent,
    4 : ButtonPressEvent,
    5 : ButtonReleaseEvent,
    6 : MotionEvent,
    7 : EnterEvent,
    8 : LeaveEvent,
    9 : FocusInEvent,
    10 : FocusOutEvent,
    11 : HierarchyEvent,
    12 : PropertyEvent,
    13 : RawKeyPressEvent,
    14 : RawKeyReleaseEvent,
    15 : RawButtonPressEvent,
    16 : RawButtonReleaseEvent,
    17 : RawMotionEvent,
    18 : TouchBeginEvent,
    19 : TouchUpdateEvent,
    20 : TouchEndEvent,
    21 : TouchOwnershipEvent,
    22 : RawTouchBeginEvent,
    23 : RawTouchUpdateEvent,
    24 : RawTouchEndEvent,
    25 : BarrierHitEvent,
    26 : BarrierLeaveEvent,
}

_errors = {
    0 : (DeviceError, BadDevice),
    1 : (EventError, BadEvent),
    2 : (ModeError, BadMode),
    3 : (DeviceBusyError, BadDeviceBusy),
    4 : (ClassError, BadClass),
}

xcb._add_ext(key, xinputExtension, _events, _errors)
